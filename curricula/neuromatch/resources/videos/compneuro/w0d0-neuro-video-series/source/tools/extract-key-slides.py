#!/usr/bin/env python3
"""Extract representative slide frames from YouTube storyboard sheets.

The W0D0 source pages embed YouTube videos. YouTube exposes a storyboard of
10-second frames for each public video; this script uses that public metadata
to create a contact sheet and a compact, deduplicated set of key frames.
"""

from __future__ import annotations

import json
import math
import re
import sys
import urllib.request
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps, ImageStat


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest.json"
RAW = ROOT / "raw"
SLIDES = ROOT / "slides"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def decode_json_string(value: str) -> str:
    return json.loads(f'"{value}"')


def storyboard_metadata(video: dict) -> tuple[str, int, int, int, int, int]:
    # The local raw files preserve the Neuromatch course pages. YouTube keeps
    # storyboard metadata only on its public watch page.
    html = fetch(video["youtube_url"]).decode("utf-8")
    match = re.search(r'"spec":"(https:[^"]+storyboard[^"]+)"', html)
    if not match:
        raise RuntimeError(f"No storyboard spec found for {video['slug']}")
    spec = decode_json_string(match.group(1))
    levels = spec.split("|")
    base_url = levels[0]
    level = levels[-1].split("#")
    width, height, frame_count, cols, rows = map(int, level[:5])
    token, signature = level[6:]
    duration_match = re.search(r'"lengthSeconds":"(\d+)"', html)
    if not duration_match:
        raise RuntimeError(f"No duration found for {video['slug']}")
    # The first pipe-delimited component is the URL template, not a level.
    return base_url.replace("$L", str(len(levels) - 2)), int(duration_match.group(1)), width, height, frame_count, cols * rows, token, signature


def timestamp(seconds: float) -> str:
    seconds = int(seconds)
    return f"{seconds // 3600:02d}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"


def frame_difference(left: Image.Image, right: Image.Image) -> float:
    a = ImageOps.grayscale(left).resize((32, 18))
    b = ImageOps.grayscale(right).resize((32, 18))
    return ImageStat.Stat(ImageChops.difference(a, b)).mean[0]


def load_frames(video: dict) -> tuple[list[Image.Image], list[float]]:
    base, duration, width, height, count, per_sheet, token, signature = storyboard_metadata(video)
    frames: list[Image.Image] = []
    for sheet_index in range(math.ceil(count / per_sheet)):
        url = base.replace("$N", token).replace("$M", str(sheet_index)) + f"&sigh={signature}"
        sheet = Image.open(BytesIO(fetch(url))).convert("RGB")
        cols = sheet.width // width
        rows = sheet.height // height
        for row in range(rows):
            for col in range(cols):
                if len(frames) >= count:
                    break
                frames.append(sheet.crop((col * width, row * height, (col + 1) * width, (row + 1) * height)))
    interval = duration / count
    return frames, [index * interval for index in range(len(frames))]


def key_indices(frames: list[Image.Image]) -> list[int]:
    # Preserve section coverage, then add visually distinct slides. The threshold
    # was tuned for the 160x90 YouTube storyboard level to ignore cursor motion.
    anchors = {round(index * (len(frames) - 1) / 8) for index in range(9)}
    selected = {0, len(frames) - 1, *anchors}
    previous = frames[0]
    for index, frame in enumerate(frames[1:], start=1):
        if frame_difference(previous, frame) >= 19:
            selected.add(index)
            previous = frame
    # Consecutive transition frames often show the same slide fade. Keep a
    # stable frame at least 20 seconds after the preceding selected frame.
    ordered = sorted(selected)
    compact: list[int] = []
    for index in ordered:
        if not compact or index - compact[-1] >= 2 or index in anchors:
            compact.append(index)
    return compact


def annotated(frame: Image.Image, label: str, scale: int = 4) -> Image.Image:
    image = frame.resize((frame.width * scale, frame.height * scale), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(size=16)
    draw.rectangle((0, 0, 135, 24), fill="black")
    draw.text((6, 5), label, fill="white", font=font)
    return image


def make_contact_sheet(frames: list[Image.Image], times: list[float], output: Path) -> None:
    cols = 5
    tiles = [annotated(frame, timestamp(time), scale=2) for frame, time in zip(frames, times)]
    rows = math.ceil(len(tiles) / cols)
    sheet = Image.new("RGB", (cols * tiles[0].width, rows * tiles[0].height), "white")
    for index, tile in enumerate(tiles):
        sheet.paste(tile, ((index % cols) * tile.width, (index // cols) * tile.height))
    sheet.save(output, quality=92)


def extract(video: dict) -> dict:
    frames, times = load_frames(video)
    video_dir = SLIDES / video["slug"]
    video_dir.mkdir(parents=True, exist_ok=True)
    make_contact_sheet(frames, times, video_dir / "contact-sheet.jpg")
    entries = []
    for position, index in enumerate(key_indices(frames), start=1):
        time = times[index]
        name = f"{position:02d}-{timestamp(time).replace(':', '-')}.jpg"
        annotated(frames[index], timestamp(time)).save(video_dir / name, quality=95)
        entries.append({"file": name, "timestamp": timestamp(time), "seconds": round(time, 1), "storyboard_index": index})
    (video_dir / "index.json").write_text(json.dumps({"video": video["slug"], "frame_count": len(frames), "key_frames": entries}, indent=2) + "\n", encoding="utf-8")
    return {"slug": video["slug"], "title": video["title"], "key_frame_count": len(entries), "frames": entries}


def main() -> None:
    videos = json.loads(MANIFEST.read_text(encoding="utf-8"))
    SLIDES.mkdir(exist_ok=True)
    report = [extract(video) for video in videos]
    (SLIDES / "index.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
