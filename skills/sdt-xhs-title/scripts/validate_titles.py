#!/usr/bin/env python3
"""Validate SDT Xiaohongshu title lengths."""

from __future__ import annotations

import argparse
import json


def inspect(title: str, limit: int) -> dict[str, object]:
    cleaned = title.strip()
    length = len(cleaned)
    return {
        "title": cleaned,
        "length": length,
        "limit": limit,
        "valid": 0 < length <= limit,
        "over_by": max(0, length - limit),
    }


def self_test() -> None:
    assert inspect("真正属于你的时间有多少", 20)["valid"] is True
    assert inspect("这是一个明显超过二十个字符而且无法直接使用的小红书标题", 20)["valid"] is False
    assert inspect("", 20)["valid"] is False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("titles", nargs="*")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("validate_titles: ok")
        return 0

    if args.limit < 1:
        parser.error("--limit must be positive")
    print(
        json.dumps(
            [inspect(title, args.limit) for title in args.titles],
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

