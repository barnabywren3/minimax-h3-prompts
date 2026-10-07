"""Every card must be a request MiniMax H3 accepts, and the README must match prompts.json."""
import json
import os
import re
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import run_prompt  # noqa: E402

LIB = run_prompt.library()
CARDS = LIB["cards"]
FIXED = {"21:9", "16:9", "4:3", "1:1", "3:4", "9:16"}


def test_ids_are_unique_and_there_are_at_least_30():
    ids = [c["id"] for c in CARDS]
    assert len(ids) == len(set(ids)) and len(ids) >= 30


@pytest.mark.parametrize("card", CARDS, ids=[c["id"] for c in CARDS])
def test_card_fits_minimax_h3(card):
    assert card["mode"] in {"text", "reference", "first_frame", "first_last_frame"}
    assert isinstance(card["duration"], int) and 4 <= card["duration"] <= 15
    assert card["resolution"] in LIB["usd_per_second"]
    assert 0 < len(card["prompt"]) <= 7000 and card["notes"]
    refs = card.get("references", [])
    counts = {k: sum(1 for r in refs if r["kind"] == k) for k in ("image", "video", "audio")}
    if card["mode"] in ("first_frame", "first_last_frame"):
        assert not refs and "aspect_ratio" not in card
        assert len(card["frames"]) == (1 if card["mode"] == "first_frame" else 2)
        assert "@" not in card["prompt"]
        return
    if card["mode"] == "text":
        assert not refs and card["aspect_ratio"] in FIXED
    else:
        assert refs and (card["aspect_ratio"] in FIXED or card["aspect_ratio"] == "adaptive")
    assert counts["image"] <= 9 and counts["video"] <= 3 and counts["audio"] <= 3 and sum(counts.values()) <= 12
    assert not counts["audio"] or counts["image"] or counts["video"], "audio needs an image or video"
    for r in refs:
        if r["kind"] == "video":
            assert 2 <= r["seconds"] <= 15
    for tag, n in re.findall(r"@(Image|Video|Audio) (\d+)", card["prompt"]):
        assert 1 <= int(n) <= counts[tag.lower()], f"@{tag} {n} has no matching reference"


def test_costs_include_reference_clip_seconds():
    dance = run_prompt.card_by_id("motion-01")
    assert run_prompt.billed_seconds(dance) == 8 + 6
    assert run_prompt.cost(dance) == pytest.approx(14 * 0.039)


def test_build_requires_the_assets_a_card_needs():
    with pytest.raises(SystemExit):
        run_prompt.build(run_prompt.card_by_id("motion-03"), images=["https://a.test/me.png"])
    body = run_prompt.build(run_prompt.card_by_id("frames-03"), first="https://a.test/d.png", last="https://a.test/n.png")
    assert body["aspect_ratio"] == "adaptive" and body["end_image"] == {"url": "https://a.test/n.png"}


def test_readme_is_in_sync_with_the_library():
    readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    index = readme.split("<!-- index:start -->\n")[1].split("\n<!-- index:end -->")[0]
    cards = readme.split("<!-- cards:start -->\n")[1].split("\n<!-- cards:end -->")[0]
    assert index == run_prompt.readme_index(LIB)
    assert cards == run_prompt.readme_cards(LIB).strip()
