#!/usr/bin/env python3
"""Browse, price and run the MiniMax H3 prompt cards in prompts.json.

    python3 run_prompt.py list                         # id, mode, settings and cost of every card
    python3 run_prompt.py show motion-03               # the full card
    python3 run_prompt.py run product-01 --dry-run     # the exact request body, nothing sent
    python3 run_prompt.py run motion-03 --image me.png --audio line.mp3 --out me.mp4
    python3 run_prompt.py readme                       # regenerate the README index and cards

Reference cards need their assets: --image / --video / --audio (repeatable, in @-number
order); frame cards need --first (and --last). Local files are uploaded first.
Standard library only; MINIMAX_H3_API_KEY (and optionally MINIMAX_H3_BASE_URL) to run.
"""
import argparse
import json
import math
import os
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
LIBRARY = os.path.join(HERE, "prompts.json")
MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".mp4": "video/mp4",
        ".mov": "video/quicktime", ".mp3": "audio/mpeg", ".wav": "audio/wav"}
FIELD = {"image": "reference_images", "video": "reference_videos", "audio": "reference_audios"}
USER_AGENT = "minimax-h3-prompts/1.0"  # sent on every request, including upload PUTs


def library():
    with open(LIBRARY, encoding="utf-8") as fh:
        return json.load(fh)


def card_by_id(card_id):
    for card in library()["cards"]:
        if card["id"] == card_id:
            return card
    raise SystemExit(f"no card {card_id!r}; see `python3 run_prompt.py list`")


def billed_seconds(card):
    ref = sum(r.get("seconds", 0) for r in card.get("references", []) if r["kind"] == "video")
    return card["duration"] + math.floor(ref)


def cost(card, rates=None):
    rates = rates or library()["usd_per_second"]
    return round(billed_seconds(card) * rates[card["resolution"]], 4)


def settings(card):
    ratio = card.get("aspect_ratio") or "adaptive"
    return f"{card['duration']} s · {card['resolution']} · {ratio}"


def needs(card):
    if card["mode"] in ("first_frame", "first_last_frame"):
        return " + ".join(card["frames"])
    refs = card.get("references", [])
    return ", ".join(f"{r['kind']}: {r['role']}" for r in refs) or "—"


def build(card, images=(), videos=(), audios=(), first=None, last=None, resolution=None):
    body = {"model": "minimax-h3", "prompt": card["prompt"], "duration": card["duration"],
            "resolution": resolution or card["resolution"]}
    if card["mode"] in ("first_frame", "first_last_frame"):
        if not first or (card["mode"] == "first_last_frame" and not last):
            raise SystemExit(f"{card['id']} needs --first" + (" and --last" if card["mode"] == "first_last_frame" else ""))
        body["aspect_ratio"] = "adaptive"
        body["start_image"] = {"url": first}
        if last:
            body["end_image"] = {"url": last}
        return body
    body["aspect_ratio"] = card["aspect_ratio"]
    given = {"image": list(images), "video": list(videos), "audio": list(audios)}
    for kind in FIELD:
        wanted = sum(1 for r in card.get("references", []) if r["kind"] == kind)
        if len(given[kind]) != wanted:
            raise SystemExit(f"{card['id']} needs {wanted} --{kind} value(s), got {len(given[kind])}")
        if wanted:
            body[FIELD[kind]] = [{"url": u} for u in given[kind]]
    return body


# --------------------------------------------------------------- running a card

def call(method, url, payload=None, raw=False, auth=True, ctype=None):
    req = urllib.request.Request(url, method=method,
                                 data=payload if isinstance(payload, bytes) or payload is None else json.dumps(payload).encode())
    req.add_header("User-Agent", USER_AGENT)
    if auth:
        req.add_header("Authorization", "Bearer " + os.environ["MINIMAX_H3_API_KEY"])
    if ctype or (payload is not None and not isinstance(payload, bytes)):
        req.add_header("Content-Type", ctype or "application/json")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
    except urllib.error.HTTPError as err:
        raise SystemExit(f"HTTP {err.code} on {method}: {err.read().decode('utf-8', 'replace')[:300]}")
    return data if raw else json.loads(data)


def to_url(value, base):
    if value is None or value.startswith("https://"):
        return value
    ctype = MIME.get(os.path.splitext(value)[1].lower())
    if not ctype:
        raise SystemExit(f"{value}: use PNG/JPEG, MP4/MOV or MP3/WAV")
    ticket = call("POST", base + "/media/uploads", {"model": "minimax-h3", "type": ctype.split("/")[0],
                                                     "content_type": ctype, "size_bytes": os.path.getsize(value)})
    with open(value, "rb") as fh:
        call("PUT", ticket["upload_url"], fh.read(), raw=True, auth=False, ctype=ctype)
    return ticket["media_url"]


def run(card, args):
    base = os.environ.get("MINIMAX_H3_BASE_URL", "https://argolink.io/v1").rstrip("/")
    preview = build(card, args.image, args.video, args.audio, args.first, args.last, args.resolution)
    rate = library()["usd_per_second"][preview["resolution"]]
    estimate = (preview["duration"] + math.floor(sum(r.get("seconds", 0) for r in card.get("references", [])
                                                     if r["kind"] == "video"))) * rate
    if args.dry_run:
        print(json.dumps(preview, indent=2))
        print(f"estimated cost: ${estimate:.3f}", file=sys.stderr)
        return
    if "MINIMAX_H3_API_KEY" not in os.environ:
        raise SystemExit("export MINIMAX_H3_API_KEY first (or use --dry-run)")
    body = build(card, [to_url(v, base) for v in args.image], [to_url(v, base) for v in args.video],
                 [to_url(v, base) for v in args.audio], to_url(args.first, base), to_url(args.last, base),
                 args.resolution)
    request_id = call("POST", base + "/videos/generations", body)["request_id"]
    print(f"{card['id']}: {request_id}", file=sys.stderr)
    while True:
        job = call("GET", f"{base}/videos/{request_id}")
        if job["status"] == "done":
            break
        if job["status"] in ("failed", "expired"):
            raise SystemExit(f"{job['status']}: {job.get('error')} (not billed)")
        print(f"{job['status']} {job.get('progress', 0)}%", file=sys.stderr)
        time.sleep(10)
    out = args.out or f"{card['id']}.mp4"
    with open(out, "wb") as fh:
        fh.write(call("GET", f"{base}/videos/{request_id}/content", raw=True))
    print(json.dumps({"file": out, "usage": job.get("usage")}))


# --------------------------------------------------------------- README sections

def readme_index(lib):
    rows = ["| # | Card | Category | Mode | Settings | Cost |", "|---:|---|---|---|---|---:|"]
    for n, card in enumerate(lib["cards"], 1):
        rows.append(f"| {n} | [{card['title']}](#{card['id']}) | {card['category']} | {card['mode'].replace('_', ' ')} "
                    f"| {settings(card)} | ${cost(card, lib['usd_per_second']):.3f} |")
    return "\n".join(rows)


def readme_cards(lib):
    out, category = [], None
    for card in lib["cards"]:
        if card["category"] != category:
            category = card["category"]
            out.append(f"### {category}\n")
        out.append(f'<a id="{card["id"]}"></a>\n**{card["title"]}** · `{card["id"]}` · {settings(card)} · '
                   f'${cost(card, lib["usd_per_second"]):.3f}  \nNeeds: {needs(card)}\n\n```text\n{card["prompt"]}\n```\n'
                   f'{card["notes"]}\n')
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="MiniMax H3 prompt cards")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    sub.add_parser("readme")
    show = sub.add_parser("show")
    show.add_argument("id")
    runp = sub.add_parser("run")
    runp.add_argument("id")
    for kind in ("image", "video", "audio"):
        runp.add_argument(f"--{kind}", action="append", default=[])
    runp.add_argument("--first")
    runp.add_argument("--last")
    runp.add_argument("--resolution", choices=["768p", "2k"], help="override the card's tier")
    runp.add_argument("--out")
    runp.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    lib = library()
    if a.cmd == "list":
        for card in lib["cards"]:
            print(f"{card['id']:<14} {card['mode']:<17} {settings(card):<26} ${cost(card, lib['usd_per_second']):.3f}  {card['title']}")
    elif a.cmd == "readme":
        print(readme_index(lib) + "\n\n" + readme_cards(lib))
    elif a.cmd == "show":
        print(json.dumps(card_by_id(a.id), indent=2, ensure_ascii=False))
    else:
        if a.dry_run:
            stand_in = lambda v: v if v is None or v.startswith("https://") else "https://upload.invalid/" + os.path.basename(v)
            a.image, a.video, a.audio = [stand_in(v) for v in a.image], [stand_in(v) for v in a.video], [stand_in(v) for v in a.audio]
            a.first, a.last = stand_in(a.first), stand_in(a.last)
        run(card_by_id(a.id), a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
