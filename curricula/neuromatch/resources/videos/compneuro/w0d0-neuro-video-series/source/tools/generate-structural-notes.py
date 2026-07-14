#!/usr/bin/env python3
"""Generate bilingual structural notes from the W0D0 caption summaries.

Requires an Anthropic-compatible endpoint through ANTHROPIC_BASE_URL and
ANTHROPIC_AUTH_TOKEN. The generated notes are explicitly marked as drafts.
"""

from __future__ import annotations

import json
import os
import urllib.request
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest.json"
SUMMARIES = ROOT / "summaries"
SLIDES = ROOT / "slides"
OUTPUT = ROOT / "structural"


PROMPT = """You are preparing a bilingual structural learning note for one Neuromatch computational neuroscience video.
Use only the provided timestamped bilingual captions. Do not invent facts, citations, numerical values, methods, or claims beyond those captions. This is a draft-learning artifact, not a primary scientific source.

Write compact Markdown, with every substantive point in Chinese followed immediately by an English translation. Use precisely these sections and no level-1 title:
## Core Problem / 核心问题
## Thesis / 核心论点
## Argument Structure / 论证结构
Use 4-7 numbered items. Each item must have a timestamp range, the role in the argument, then a Chinese statement and its English translation.
## Mechanism and Objects / 机制与对象
State any biological mechanism, measurement signal, mathematical or computational object actually introduced. Separate established teaching content from a stated interpretation when necessary.
## Evidence and Method / 证据与方法
## Limits and Misconceptions / 局限与易错点
## NeuroAI Connection / NeuroAI 连接
Mark connections to AI as interpretation or analogy, not as a claim of equivalence.
## Review Questions / 复习问题
Give three bilingual questions.
## Key Slide Guide / 关键幻灯片导读
Make a compact table with `Time`, `Role`, and `Bilingual cue`. Cover the supplied candidate frame timestamps by grouping adjacent timestamps when they serve the same idea.

Caption summary follows:
"""


def call_model(prompt: str) -> str:
    base = os.environ["ANTHROPIC_BASE_URL"].rstrip("/")
    token = os.environ["ANTHROPIC_AUTH_TOKEN"]
    model = os.environ.get("ANTHROPIC_DEFAULT_HAIKU_MODEL", os.environ["ANTHROPIC_DEFAULT_SONNET_MODEL"])
    body = json.dumps({
        "model": model,
        "max_tokens": 3600,
        "temperature": 0.2,
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")
    request = urllib.request.Request(
        f"{base}/v1/messages",
        data=body,
        headers={
            "Content-Type": "application/json",
            "x-api-key": token,
            "anthropic-version": "2023-06-01",
        },
    )
    with urllib.request.urlopen(request, timeout=240) as response:
        payload = json.load(response)
    text = "".join(part.get("text", "") for part in payload.get("content", []) if part.get("type") == "text").strip()
    if not text:
        kinds = [part.get("type", "unknown") for part in payload.get("content", [])]
        raise RuntimeError(f"The model emitted no text blocks (content types: {kinds})")
    return text


def slide_gallery(video: dict) -> str:
    frame_index = json.loads((SLIDES / video["slug"] / "index.json").read_text(encoding="utf-8"))
    lines = ["## Key Slide Screenshots / 关键幻灯片截图", "", "These are representative frames from YouTube's public 10-second storyboard, not original-resolution stills. / 以下为 YouTube 公开 10 秒分镜中的代表帧，并非原始分辨率截图。", ""]
    for frame in frame_index["key_frames"]:
        path = f"../slides/{video['slug']}/{frame['file']}"
        lines.extend([f"### {frame['timestamp']}", "", f"![Video storyboard frame at {frame['timestamp']}]({path})", ""])
    lines.extend(["## Full Timeline Contact Sheet / 完整时间线联系表", "", f"![Storyboard contact sheet](../slides/{video['slug']}/contact-sheet.jpg)", ""])
    return "\n".join(lines)


def generate(video: dict) -> None:
    summary_path = SUMMARIES / f"{video['slug']}.summary.bilingual.md"
    summary = summary_path.read_text(encoding="utf-8")
    content = call_model(PROMPT + "\n" + summary)
    if not content:
        raise RuntimeError(f"The model returned no note for {video['slug']}")
    header = f"# W0D0 {video['title']} - Structural Note / 结构化笔记\n\n"
    source = (
        f"- Status / 状态: AI-generated draft based on the video captions; verify important scientific claims against primary sources. / 基于视频字幕生成的 AI 草稿；重要科学主张需回查一手来源。\n"
        f"- Course page / 课程页: {video['source_page']}\n"
        f"- Video / 视频: {video['youtube_url']}\n"
        f"- Caption basis / 字幕依据: `../summaries/{video['slug']}.summary.bilingual.md`\n\n"
    )
    for heading in (
        "Core Problem / 核心问题",
        "Thesis / 核心论点",
        "Argument Structure / 论证结构",
        "Mechanism and Objects / 机制与对象",
        "Evidence and Method / 证据与方法",
        "Limits and Misconceptions / 局限与易错点",
        "NeuroAI Connection / NeuroAI 连接",
        "Review Questions / 复习问题",
        "Key Slide Guide / 关键幻灯片导读",
    ):
        content = content.replace(f"# {heading}", f"## {heading}")
    (OUTPUT / f"{video['slug']}.structural.md").write_text(header + source + content + "\n\n" + slide_gallery(video), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", help="Generate a note for one video slug only.")
    args = parser.parse_args()
    OUTPUT.mkdir(exist_ok=True)
    videos = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if args.slug:
        videos = [video for video in videos if video["slug"] == args.slug]
        if not videos:
            raise SystemExit(f"Unknown video slug: {args.slug}")
    for index, video in enumerate(videos, start=1):
        print(f"[{index}/{len(videos)}] {video['slug']}", flush=True)
        generate(video)


if __name__ == "__main__":
    main()
