# Naruto Bros - Konoha Platformer

Mario-style pixel platformer with a Naruto concept. Runs in the browser, works on phone (touch controls) and PC.

**Play:** open `index.html` (or the deployed link). Add `?demo=1` to the URL for autoplay demo mode.

## How to play
- Move: Arrows / WASD (touch: on-screen buttons)
- Jump: Space / W / A-button. Press again mid-air for DOUBLE JUMP (chakra step)
- Attack: X / J / B-button. Base form throws kunai, Sage Mode throws a bouncing RASENGAN
- Grab the Sage Scroll from ? blocks to enter Sage Mode (breaks bricks, extra hit)
- Ramen = 1UP. Stomp enemies, avoid the spiky ones. Reach the flag!

3 playable ninjas on the title screen (pick with arrows): NARUTO (balanced), SASUKE (faster), KAKASHI (higher jump).

## Swapping sprites (data-driven)
Everything visual lives in `sprites/` and is wired by `sprites/manifest.json`:
`character -> animation -> frames`. Frames can be PNG folders (`frames: [...]`) or slices of a sheet (`sheet`, `fw`, `fh`, `row`, `cols`).
Frames are drawn anchored bottom-center, so any frame size works. To add a character: drop its art in `sprites/chars/`, add an entry under `characters`, done - it appears on the select screen. `speed` / `jump` tune its physics.

Want per-animation folders with many ripped frames? That's the personal build - ask Instinct for the "personal sprite pack" zip.

## Art note
All sprites in THIS repo are original pixel art (generated with `gen_sprites.py`), not ripped game assets - safe to keep public.
