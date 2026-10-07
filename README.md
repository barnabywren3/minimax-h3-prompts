# MiniMax H3 Prompts — 36 video prompt cards with settings and cost

36 prompt cards for MiniMax H3 (`minimax-h3`), written to the model's published limits. Each card gives the prompt, the duration, resolution tier and aspect ratio to send, the images, clips, audio or frames it needs, and what one run costs. No sample renders are bundled: run a card and judge the result yourself.

[How to write for H3](#how-to-write-for-minimax-h3) · [Index](#index) · [Cards](#cards) · [Run a card](#run-a-card) · [Add a card](#add-a-card)

<sub>Last checked: 2026-10-07. Every card passes the validation in `tests/`.</sub>

## How to write for MiniMax H3

| Rule | Why |
|---|---|
| Shot type, subject, one action, camera move, place and light, then sound | the model gets one clear event and a camera plan |
| Describe the sound you want | every H3 video carries a generated stereo soundtrack; there is no silent option |
| Put spoken lines in quotes and say who speaks | dialogue is generated with the picture |
| Point at assets as `@Image 1`, `@Video 1`, `@Audio 1` | numbers follow the order of each list; unnamed assets are still used |
| Audio needs an image or video beside it | audio-only references are rejected |
| Frame prompts describe the change, not the pictures | the first (and last) frame already fix the look; the shape follows the first frame |
| Skip small on-screen text | generated lettering can come out garbled; add titles in editing |
| Draft at 768p, ship at 2K | 2K costs about 1.6× as much per second |

Limits behind the cards: 4–15 s; `768p` or `2k`; ratios 21:9, 16:9, 4:3, 1:1, 3:4, 9:16 (frame modes follow the first frame); up to 9 images, 3 clips and 3 audio tracks, 12 in total, clips and tracks 2–15 s each; prompt up to 7,000 characters. Reference clip seconds are billed like output seconds; images and audio are free.

Card fields: **Settings** = duration · tier · ratio. **Needs** = the assets to pass, in @-number order. **Cost** = (duration + reference clip seconds) × the per-second rate in [Run a card](#run-a-card).

## Index

<!-- index:start -->
| # | Card | Category | Mode | Settings | Cost |
|---:|---|---|---|---|---:|
| 1 | [Perfume in falling petals](#product-01) | Product & ads | text | 6 s · 2k · 9:16 | $0.384 |
| 2 | [Your product on a turntable](#product-02) | Product & ads | reference | 5 s · 768p · 1:1 | $0.195 |
| 3 | [Sneaker unboxing, handheld](#product-03) | Product & ads | text | 8 s · 768p · 9:16 | $0.312 |
| 4 | [Skincare texture close-up](#product-04) | Product & ads | text | 5 s · 2k · 3:4 | $0.320 |
| 5 | [Watch reveal from shadow](#product-05) | Product & ads | text | 6 s · 2k · 16:9 | $0.384 |
| 6 | [Street interview](#dialogue-01) | Dialogue & talking heads | text | 8 s · 768p · 9:16 | $0.312 |
| 7 | [Two people, one kitchen argument](#dialogue-02) | Dialogue & talking heads | text | 10 s · 768p · 16:9 | $0.390 |
| 8 | [Studio news anchor](#dialogue-03) | Dialogue & talking heads | text | 7 s · 2k · 16:9 | $0.448 |
| 9 | [Your presenter, new script](#dialogue-04) | Dialogue & talking heads | reference | 10 s · 768p · 9:16 | $0.390 |
| 10 | [Multilingual greeting](#dialogue-05) | Dialogue & talking heads | text | 6 s · 768p · 1:1 | $0.234 |
| 11 | [Storm over a wheat field](#cinematic-01) | Cinematic & nature | text | 10 s · 2k · 21:9 | $0.640 |
| 12 | [Whale breach at dawn](#cinematic-02) | Cinematic & nature | text | 6 s · 2k · 16:9 | $0.384 |
| 13 | [Desert caravan at dusk](#cinematic-03) | Cinematic & nature | text | 12 s · 768p · 21:9 | $0.468 |
| 14 | [Rain on a city window](#cinematic-04) | Cinematic & nature | text | 8 s · 768p · 9:16 | $0.312 |
| 15 | [Northern lights over a cabin](#cinematic-05) | Cinematic & nature | text | 10 s · 2k · 16:9 | $0.640 |
| 16 | [Rooftop parkour](#action-01) | Action & sports | text | 7 s · 768p · 16:9 | $0.273 |
| 17 | [Kickflip in slow motion](#action-02) | Action & sports | text | 5 s · 2k · 9:16 | $0.320 |
| 18 | [Boxing pads, sweat and light](#action-03) | Action & sports | text | 6 s · 768p · 4:3 | $0.234 |
| 19 | [Sprint start](#action-04) | Action & sports | text | 4 s · 768p · 16:9 | $0.156 |
| 20 | [Same character, new place](#character-01) | Reference: characters & products | reference | 8 s · 768p · 16:9 | $0.312 |
| 21 | [Two characters meet](#character-02) | Reference: characters & products | reference | 8 s · 768p · 16:9 | $0.312 |
| 22 | [Outfit from a second image](#character-03) | Reference: characters & products | reference | 6 s · 768p · 9:16 | $0.234 |
| 23 | [Product in a real setting](#character-04) | Reference: characters & products | reference | 6 s · 2k · 16:9 | $0.384 |
| 24 | [Copy a dance](#motion-01) | Reference: motion & sound | reference | 8 s · 768p · 9:16 | $0.546 |
| 25 | [Borrow a camera move](#motion-02) | Reference: motion & sound | reference | 6 s · 768p · 16:9 | $0.390 |
| 26 | [Lip-sync to your voice](#motion-03) | Reference: motion & sound | reference | 8 s · 768p · 9:16 | $0.312 |
| 27 | [Cut to the beat](#motion-04) | Reference: motion & sound | reference | 10 s · 768p · 9:16 | $0.390 |
| 28 | [Bring a painting to life](#frames-01) | First frame & first+last frame | first frame | 6 s · 768p · adaptive | $0.234 |
| 29 | [Old family photo, gently animated](#frames-02) | First frame & first+last frame | first frame | 5 s · 768p · adaptive | $0.195 |
| 30 | [Day to night, same skyline](#frames-03) | First frame & first+last frame | first last frame | 8 s · 2k · adaptive | $0.512 |
| 31 | [Sketch becomes the render](#frames-04) | First frame & first+last frame | first last frame | 6 s · 768p · adaptive | $0.234 |
| 32 | [Logo reveal between two frames](#frames-05) | First frame & first+last frame | first last frame | 4 s · 2k · adaptive | $0.256 |
| 33 | [Claymation breakfast](#stylized-01) | Stylized & animation | text | 6 s · 768p · 4:3 | $0.234 |
| 34 | [Paper cut-out forest](#stylized-02) | Stylized & animation | text | 8 s · 768p · 16:9 | $0.312 |
| 35 | [Anime rooftop duel](#stylized-03) | Stylized & animation | text | 8 s · 2k · 16:9 | $0.512 |
| 36 | [3D toy commercial](#stylized-04) | Stylized & animation | text | 6 s · 768p · 1:1 | $0.234 |
<!-- index:end -->

## Cards

<!-- cards:start -->
### Product & ads

<a id="product-01"></a>
**Perfume in falling petals** · `product-01` · 6 s · 2k · 9:16 · $0.384  
Needs: —

```text
Slow-motion macro of a faceted glass perfume bottle on black velvet while pale pink petals fall around it. One petal slides down the glass. The camera arcs a quarter turn to catch a rim of gold light on the cap. Hushed room tone, a single soft chime as the petal lands.
```
Text mode invents the bottle. For your own bottle, use product-02's reference setup.

<a id="product-02"></a>
**Your product on a turntable** · `product-02` · 5 s · 768p · 1:1 · $0.195  
Needs: image: clean front shot of the product

```text
@Image 1 rotates slowly on a white marble turntable under soft studio light, a thin reflection on the surface. The label stays sharp and readable through the full turn. Faint motor hum, no music.
```
Say what must not change (label, color). A plain background in the reference image keeps the focus on the product.

<a id="product-03"></a>
**Sneaker unboxing, handheld** · `product-03` · 8 s · 768p · 9:16 · $0.312  
Needs: —

```text
Handheld phone-style shot: two hands lift the lid of an orange shoebox on a bedroom floor, push back tissue paper and pull out a white running shoe, turning it toward the camera. Tissue rustle, a delighted "Finally!" off camera. Daylight from a window.
```
Naming the camera style (handheld, phone) steers it toward a user-generated look.

<a id="product-04"></a>
**Skincare texture close-up** · `product-04` · 5 s · 2k · 3:4 · $0.320  
Needs: —

```text
Extreme close-up: a fingertip swirls a dollop of pearly cream on frosted glass, the texture folding into soft peaks. Raking side light shows the shimmer. Quiet, a soft squish.
```
4:5 is not an H3 ratio; 3:4 is the nearest portrait option.

<a id="product-05"></a>
**Watch reveal from shadow** · `product-05` · 6 s · 2k · 16:9 · $0.384  
Needs: —

```text
Darkness, then a thin line of light sweeps across a steel wristwatch on a slate slab, revealing the dial and the second hand ticking. The camera pushes in until the bezel fills the frame. Every tick is audible, then a low synth swell.
```
A light sweep reveals detail without a fast camera move.

### Dialogue & talking heads

<a id="dialogue-01"></a>
**Street interview** · `dialogue-01` · 8 s · 768p · 9:16 · $0.312  
Needs: —

```text
Vox-pop on a busy sidewalk: a young man in a denim jacket looks into a handheld microphone and says "Honestly? I'd take the train every day if it ran on time." Passers-by blur behind him, traffic noise, the interviewer laughs.
```
Put the exact line in quotes and give the speaker a clear look; the soundtrack is generated with the picture.

<a id="dialogue-02"></a>
**Two people, one kitchen argument** · `dialogue-02` · 10 s · 768p · 16:9 · $0.390  
Needs: —

```text
Medium two-shot in a narrow kitchen at night. A woman sets down a mug hard and says "You said you'd call." The man by the fridge answers quietly, "I know. I'm sorry." Fridge hum, a clock ticking, warm pendant light, the camera drifts slowly between them.
```
Attribute each line to a described person and keep the exchange to two lines in 10 s.

<a id="dialogue-03"></a>
**Studio news anchor** · `dialogue-03` · 7 s · 2k · 16:9 · $0.448  
Needs: —

```text
A news anchor in a navy suit at a glass desk looks into the lens and says "Good evening. Tonight: the city votes on a four-day school week." Blue studio lighting, a monitor wall behind her, a short news sting at the start.
```
Keep on-screen text out of the prompt and add it in editing.

<a id="dialogue-04"></a>
**Your presenter, new script** · `dialogue-04` · 10 s · 768p · 9:16 · $0.390  
Needs: image: the presenter, chest-up, facing camera

```text
@Image 1 sits at a tidy desk with a laptop and says to camera "Three things I wish I knew before my first marathon." She counts on her fingers as she talks. Soft key light, plants behind her, a quiet room.
```
Use a single clear face rather than a group photo.

<a id="dialogue-05"></a>
**Multilingual greeting** · `dialogue-05` · 6 s · 768p · 1:1 · $0.234  
Needs: —

```text
A smiling hotel receptionist behind a wooden counter greets the camera: "Bienvenue, welcome, willkommen." She slides a key card forward. Lobby murmur, soft piano in the distance.
```
Short mixed-language lines are a quick way to hear how the voice handles each language before you commit to a script.

### Cinematic & nature

<a id="cinematic-01"></a>
**Storm over a wheat field** · `cinematic-01` · 10 s · 2k · 21:9 · $0.640  
Needs: —

```text
Ultra-wide shot: a black thunderstorm rolls over a golden wheat field at sunset, lightning forks on the horizon, the wheat bends in waves toward the camera. Slow dolly forward. Rolling thunder, wind hiss.
```
21:9 with a slow dolly suits wide landscapes.

<a id="cinematic-02"></a>
**Whale breach at dawn** · `cinematic-02` · 6 s · 2k · 16:9 · $0.384  
Needs: —

```text
From a small boat at dawn, a humpback whale breaches close by, water sheeting off its fins, then crashes back in a burst of spray that hits the lens. Gulls, the boat engine idling, people gasping.
```
Ending on spray on the lens gives a natural cut point.

<a id="cinematic-03"></a>
**Desert caravan at dusk** · `cinematic-03` · 12 s · 768p · 21:9 · $0.468  
Needs: —

```text
A camel caravan crosses a dune ridge in silhouette against an orange sky, long shadows stretching down the sand. The camera tracks sideways at the same pace. Soft bells, wind, a distant voice calling.
```
For a 12-second take, keep one continuous motion: here a matched sideways track.

<a id="cinematic-04"></a>
**Rain on a city window** · `cinematic-04` · 8 s · 768p · 9:16 · $0.312  
Needs: —

```text
Close-up of raindrops racing down a window at night, the city lights behind them turning into bokeh circles. Focus pulls from the drops to a tram passing below. Rain patter, muffled traffic.
```
A focus pull gives a vertical frame movement without a cramped pan.

<a id="cinematic-05"></a>
**Northern lights over a cabin** · `cinematic-05` · 10 s · 2k · 16:9 · $0.640  
Needs: —

```text
A small red cabin in snow under a sky of green and violet aurora that ripples and folds. Smoke curls from the chimney; the camera tilts up slowly from the cabin to the sky. Deep silence, snow creaking.
```
Name the aurora's colors instead of leaving them to chance.

### Action & sports

<a id="action-01"></a>
**Rooftop parkour** · `action-01` · 7 s · 768p · 16:9 · $0.273  
Needs: —

```text
A runner in a grey hoodie sprints across a rooftop, vaults a vent, leaps the gap to the next building and rolls on landing. The camera follows on a drone, dropping as she jumps. Wind rush, footsteps, a thud on landing.
```
Keep it to one stunt chain per shot.

<a id="action-02"></a>
**Kickflip in slow motion** · `action-02` · 5 s · 2k · 9:16 · $0.320  
Needs: —

```text
Low angle at board level: a skater pops a kickflip over a crack in the pavement, the board spinning beneath him in slow motion before both feet catch it. Wheels clack, the crowd off camera cheers.
```
A low angle exaggerates the height of the trick.

<a id="action-03"></a>
**Boxing pads, sweat and light** · `action-03` · 6 s · 768p · 4:3 · $0.234  
Needs: —

```text
A boxer throws a fast one-two into her coach's pads in a dim gym; sweat flies off in a shaft of window light. Handheld close shot, the coach calling "Again!" Leather smacks, breathing.
```
4:3 crops tightly around two people sparring.

<a id="action-04"></a>
**Sprint start** · `action-04` · 4 s · 768p · 16:9 · $0.156  
Needs: —

```text
Ground-level shot of a sprinter in the blocks; the starter's pistol cracks and she explodes forward past the camera, spikes kicking up rubber crumbs. Stadium roar.
```
The 4-second minimum suits a single explosive beat.

### Reference: characters & products

<a id="character-01"></a>
**Same character, new place** · `character-01` · 8 s · 768p · 16:9 · $0.312  
Needs: image: the character, full body, plain background

```text
@Image 1 walks through a crowded night market, stops at a noodle stall and orders with a smile. The camera follows at shoulder height. Sizzling woks, chatter, lantern light.
```
Reuse the exact same image in every clip where this character appears.

<a id="character-02"></a>
**Two characters meet** · `character-02` · 8 s · 768p · 16:9 · $0.312  
Needs: image: first character, image: second character

```text
@Image 1 waits on a train platform; @Image 2 steps off the arriving train and they hug. The camera circles them slowly. Train brakes, an announcement echoing.
```
Give each character a distinct action so the prompt keeps them apart.

<a id="character-03"></a>
**Outfit from a second image** · `character-03` · 6 s · 768p · 9:16 · $0.234  
Needs: image: the person, image: the jacket on a hanger

```text
@Image 1 wears the jacket from @Image 2 and does a slow turn in front of a mirror in a bright fitting room, then smooths the lapel. Hangers clink, soft store music.
```
State which image supplies the person and which supplies the garment.

<a id="character-04"></a>
**Product in a real setting** · `character-04` · 6 s · 2k · 16:9 · $0.384  
Needs: image: the product (a backpack), image: the location photo

```text
A hiker sets @Image 1 down on the rocky summit shown in @Image 2, unzips the front pocket and pulls out a map as the wind tugs at it. Golden hour, wide lens. Wind, zipper, distant birds.
```
A location photo as a second reference shows the scene instead of describing it.

### Reference: motion & sound

<a id="motion-01"></a>
**Copy a dance** · `motion-01` · 8 s · 768p · 9:16 · $0.546  
Needs: image: the dancer, video: choreography clip

```text
@Image 1 performs the choreography of @Video 1 on a sunny basketball court, matching its timing. Fixed wide shot, sneakers squeaking.
```
The reference clip's 6 s are billed on top of the 8 s output.

<a id="motion-02"></a>
**Borrow a camera move** · `motion-02` · 6 s · 768p · 16:9 · $0.390  
Needs: video: a clip with the camera move you want

```text
Recreate the camera move of @Video 1 through a misty pine forest at dawn: the same speed, the same rise and turn. Birdsong, dripping water.
```
Keep the reference clip short (2-4 s): its seconds are billed like output.

<a id="motion-03"></a>
**Lip-sync to your voice** · `motion-03` · 8 s · 768p · 9:16 · $0.312  
Needs: image: the speaker, facing camera, audio: the voice line, 6-8 s

```text
@Image 1 speaks the words of @Audio 1 directly to camera in a quiet home office, natural head movement and blinks, soft daylight.
```
Audio references are free, but H3 needs an image or video beside them.

<a id="motion-04"></a>
**Cut to the beat** · `motion-04` · 10 s · 768p · 9:16 · $0.390  
Needs: image: location 1, image: location 2, image: location 3, audio: the track, 10 s

```text
A fast travel montage that jumps between @Image 1, @Image 2 and @Image 3 on every kick drum of @Audio 1, whip pans between places, bright summer light.
```
Up to 9 images fit in one request; each extra place is one more cut to fit in 10 s.

### First frame & first+last frame

<a id="frames-01"></a>
**Bring a painting to life** · `frames-01` · 6 s · 768p · adaptive · $0.234  
Needs: a landscape painting

```text
The painted clouds start to drift, the river ripples and a flock of birds crosses the sky while the brushstroke texture stays visible. Gentle wind, water.
```
Ask for the medium to stay visible (brushstrokes) or it may turn photographic.

<a id="frames-02"></a>
**Old family photo, gently animated** · `frames-02` · 5 s · 768p · adaptive · $0.195  
Needs: a scanned family portrait

```text
The people in the photo blink and smile softly, the child turns her head toward her mother, a breeze moves the curtain. Subtle motion only, keep the film grain.
```
Ask for subtle motion; large movements risk distorting the faces.

<a id="frames-03"></a>
**Day to night, same skyline** · `frames-03` · 8 s · 2k · adaptive · $0.512  
Needs: the skyline by day + the same skyline at night

```text
Time passes over the skyline: the sun sets, clouds race, windows light up floor by floor until the night view. Locked-off camera. City hum fades to night sounds.
```
Shoot or render both frames from the identical viewpoint.

<a id="frames-04"></a>
**Sketch becomes the render** · `frames-04` · 6 s · 768p · adaptive · $0.234  
Needs: a pencil sketch of a chair + the finished 3D render of the chair

```text
Pencil lines thicken, fill with wood grain and fabric, and the chair turns slightly as it becomes the finished render. Pencil scratching that fades to quiet.
```
Describe the change between the two pictures, not the pictures themselves.

<a id="frames-05"></a>
**Logo reveal between two frames** · `frames-05` · 4 s · 2k · adaptive · $0.256  
Needs: a dark frame with scattered gold particles + the logo on a dark background

```text
The gold particles swirl inward and lock together into the logo with a soft flash. A rising whoosh and a single bass hit.
```
The last frame pins the logo, so the clip ends on it.

### Stylized & animation

<a id="stylized-01"></a>
**Claymation breakfast** · `stylized-01` · 6 s · 768p · 4:3 · $0.234  
Needs: —

```text
Stop-motion claymation: a clay egg cracks itself onto a clay frying pan, the yolk wobbles, a little clay toast pops out of a toaster. Visible thumbprints, slightly choppy frame rate, cheerful ukulele.
```
Name the material details (thumbprints, choppy motion) that sell stop-motion.

<a id="stylized-02"></a>
**Paper cut-out forest** · `stylized-02` · 8 s · 768p · 16:9 · $0.312  
Needs: —

```text
Layered paper cut-out animation: a paper fox runs through a forest of folded paper trees, layers sliding at different speeds as the camera trucks right. Paper rustle, soft flute melody.
```
Parallax between paper layers gives depth without a 3D look.

<a id="stylized-03"></a>
**Anime rooftop duel** · `stylized-03` · 8 s · 2k · 16:9 · $0.512  
Needs: —

```text
Anime style: two swordswomen clash on a rooftop under a red moon, sparks and speed lines on each strike, cherry petals whipping past. Dramatic low angle, a beat of silence before the final strike, then a metallic ring.
```
A beat of silence before the hit gives the sound design room.

<a id="stylized-04"></a>
**3D toy commercial** · `stylized-04` · 6 s · 768p · 1:1 · $0.234  
Needs: —

```text
Glossy 3D animation: a small yellow robot toy wakes up on a kid's desk, stretches, and waves at the camera before jumping into a pencil cup. Bright playful lighting, boing sound, kids laughing.
```
Draft at 768p; save 2K for the version you ship.
<!-- cards:end -->

## Run a card

The cards run on [ArgoLink](https://argolink.io/gh-minimax-h3-prompts), where MiniMax H3 costs $0.039 per second at 768p and $0.064 at 2K; those are the rates in the cost column. Any server with the same async `/v1/videos` API works through `MINIMAX_H3_BASE_URL`.

```bash
git clone https://github.com/barnabywren3/minimax-h3-prompts && cd minimax-h3-prompts
export MINIMAX_H3_API_KEY=your-key

python3 run_prompt.py list                                   # every card with settings and cost
python3 run_prompt.py run cinematic-01 --dry-run             # print the request, send nothing
python3 run_prompt.py run cinematic-01 --out storm.mp4       # submit, wait, save
python3 run_prompt.py run motion-03 --image me.png --audio line.mp3          # local files are uploaded
python3 run_prompt.py run frames-03 --first day.png --last night.png --resolution 768p
```

Or send a card with curl: the request body is the card's `prompt`, `duration`, `resolution` and `aspect_ratio` with `"model": "minimax-h3"`, posted to `https://argolink.io/v1/videos/generations`; poll `GET /v1/videos/{request_id}` until `done`, then download `/content`.

| Per second | 768p | 2K |
|---|---:|---:|
| ArgoLink | $0.039 | $0.064 |
| [MiniMax pay-as-you-go](https://platform.minimax.io/docs/guides/pricing-paygo) (official) | $0.08 | $0.13 |
| [fal.ai](https://fal.ai/models/minimax/h3/text-to-video) | $0.06 | $0.13 |

<sub>Read 2026-10-07. At MiniMax's list price every card costs about twice its listed amount; failed or expired jobs are not billed on ArgoLink.</sub>

## Add a card

Add an object to `prompts.json`, then:

```bash
pip install pytest && pytest tests/        # checks limits, @-mentions, ratios and README sync
python3 run_prompt.py readme               # prints the index and cards to paste between the markers
```

## License

MIT
