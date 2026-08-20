#!/usr/bin/env python3
"""Render a Markdown subset as WeChat-paste-friendly inline-style HTML."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path


BASE_FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC',sans-serif"

STYLES = {
    "minimal": {"accent": "#111111", "text": "#2b2b2b", "muted": "#666666", "soft": "#f5f5f5", "bg": "#ffffff"},
    "essay": {"accent": "#3d332b", "text": "#352f2b", "muted": "#756b64", "soft": "#f7f3ee", "bg": "#fffdf9"},
    "business": {"accent": "#12355b", "text": "#243447", "muted": "#5d6d7e", "soft": "#eef4f8", "bg": "#ffffff"},
    "warm": {"accent": "#7a5132", "text": "#44372d", "muted": "#806e61", "soft": "#f7efe4", "bg": "#fffaf3"},
    "editorial": {"accent": "#8a1c1c", "text": "#2e2929", "muted": "#6f6666", "soft": "#f7eeee", "bg": "#ffffff"},
    "tech": {"accent": "#315efb", "text": "#202a3b", "muted": "#667085", "soft": "#eef3ff", "bg": "#ffffff"},
}


def element_styles(style_id: str) -> dict[str, str]:
    palette = STYLES[style_id]
    common = f"font-family:{BASE_FONT};color:{palette['text']};"
    return {
        "body": f"max-width:740px;margin:0 auto;padding:24px 22px;background-color:{palette['bg']};",
        "h1": common + f"margin:8px 0 28px;font-size:28px;line-height:1.35;font-weight:800;color:{palette['accent']};",
        "h2": common + f"margin:30px 0 14px;padding-bottom:8px;border-bottom:2px solid {palette['accent']};font-size:22px;line-height:1.45;font-weight:750;color:{palette['accent']};",
        "h3": common + "margin:24px 0 10px;font-size:18px;line-height:1.55;font-weight:700;",
        "p": common + "margin:12px 0;font-size:16px;line-height:1.85;",
        "blockquote": common + f"margin:20px 0;padding:13px 16px;border-left:3px solid {palette['accent']};background-color:{palette['soft']};font-size:16px;line-height:1.8;",
        "ul": common + "margin:12px 0;padding-left:24px;font-size:16px;line-height:1.8;",
        "ol": common + "margin:12px 0;padding-left:24px;font-size:16px;line-height:1.8;",
        "li": common + "margin:6px 0;font-size:16px;line-height:1.8;",
        "pre": common + f"margin:18px 0;padding:14px;white-space:pre-wrap;background-color:{palette['soft']};font-size:14px;line-height:1.65;",
        "code": f"font-family:ui-monospace,SFMono-Regular,Menlo,monospace;padding:1px 4px;background-color:{palette['soft']};color:{palette['accent']};font-size:0.92em;",
        "strong": f"font-weight:750;color:{palette['accent']};",
        "hr": f"margin:28px 0;border:0;border-top:1px solid {palette['muted']};",
    }


def render_inline(text: str, styles: dict[str, str]) -> str:
    escaped = html.escape(text.strip())
    escaped = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"[图片：\1]", escaped)
    escaped = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", escaped)
    escaped = re.sub(
        r"\*\*([^*]+)\*\*",
        lambda match: f'<strong style="{styles["strong"]}">{match.group(1)}</strong>',
        escaped,
    )
    escaped = re.sub(
        r"\x60([^\x60]+)\x60",
        lambda match: f'<code style="{styles["code"]}">{match.group(1)}</code>',
        escaped,
    )
    return escaped


def render_markdown(markdown: str, style_id: str) -> str:
    styles = element_styles(style_id)
    lines = markdown.splitlines()
    blocks: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    list_tag = "ul"
    code_lines: list[str] = []
    in_code = False

    def flush_paragraph() -> None:
        if paragraph:
            text = " ".join(part.strip() for part in paragraph).strip()
            if text:
                blocks.append(f'<p style="{styles["p"]}">{render_inline(text, styles)}</p>')
            paragraph.clear()

    def flush_list() -> None:
        if list_items:
            items = "".join(
                f'<li style="{styles["li"]}">{render_inline(item, styles)}</li>'
                for item in list_items
            )
            blocks.append(f'<{list_tag} style="{styles[list_tag]}">{items}</{list_tag}>')
            list_items.clear()

    for raw_line in lines:
        line = raw_line.rstrip()
        if line.startswith(chr(96) * 3):
            flush_paragraph()
            flush_list()
            if in_code:
                code = html.escape("\n".join(code_lines))
                blocks.append(
                    f'<pre style="{styles["pre"]}"><code style="{styles["code"]}">{code}</code></pre>'
                )
                code_lines.clear()
            in_code = not in_code
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            flush_paragraph()
            flush_list()
            continue
        if line == "---":
            flush_paragraph()
            flush_list()
            blocks.append(f'<hr style="{styles["hr"]}">')
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            flush_list()
            tag = f"h{len(heading.group(1))}"
            blocks.append(
                f'<{tag} style="{styles[tag]}">{render_inline(heading.group(2), styles)}</{tag}>'
            )
            continue
        if line.startswith("> "):
            flush_paragraph()
            flush_list()
            blocks.append(
                f'<blockquote style="{styles["blockquote"]}">{render_inline(line[2:], styles)}</blockquote>'
            )
            continue
        unordered = re.match(r"^[-*]\s+(.+)$", line)
        ordered = re.match(r"^\d+[.)]\s+(.+)$", line)
        if unordered or ordered:
            flush_paragraph()
            next_tag = "ul" if unordered else "ol"
            if list_items and next_tag != list_tag:
                flush_list()
            list_tag = next_tag
            list_items.append((unordered or ordered).group(1))
            continue
        if "|" in line and line.strip().startswith("|"):
            flush_paragraph()
            flush_list()
            blocks.append(
                f'<p style="{styles["p"]}">[表格：请在微信后台确认排版] {render_inline(line, styles)}</p>'
            )
            continue
        paragraph.append(line)

    if in_code:
        code = html.escape("\n".join(code_lines))
        blocks.append(f'<pre style="{styles["pre"]}"><code style="{styles["code"]}">{code}</code></pre>')
    flush_paragraph()
    flush_list()

    title_match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    title = html.escape(title_match.group(1).strip() if title_match else "公众号文章")
    body = "\n  ".join(blocks)
    return (
        "<!doctype html>\n"
        '<html lang="zh-CN">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"  <title>{title}</title>\n"
        "</head>\n"
        f'<body style="{styles["body"]}">\n  {body}\n</body>\n'
        "</html>\n"
    )


def self_test() -> None:
    rendered = render_markdown("# 标题\n\n正文有**重点**。\n\n- 项目一", "minimal")
    forbidden = ("<style", "class=", "id=", "<script", ":before", ":after")
    assert not any(token in rendered for token in forbidden)
    assert '<p style="' in rendered
    assert '<li style="' in rendered
    assert '<strong style="' in rendered


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs="?")
    parser.add_argument("--style", choices=sorted(STYLES), default="minimal")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--output-dir")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("render_wechat_html: ok")
        return 0
    if not args.source:
        parser.error("source Markdown file is required")

    source = Path(args.source).resolve()
    markdown = source.read_text(encoding="utf-8")
    output_dir = (
        Path(args.output_dir).resolve()
        if args.output_dir
        else source.parent / "公众号HTML输出"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    style_ids = sorted(STYLES) if args.all else [args.style]
    for style_id in style_ids:
        target = output_dir / f"{source.stem}_{style_id}_微信公众号版.html"
        target.write_text(render_markdown(markdown, style_id), encoding="utf-8")
        print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

