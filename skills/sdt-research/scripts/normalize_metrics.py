#!/usr/bin/env python3
"""Normalize public social-media metric strings without inventing missing values."""

from __future__ import annotations

import argparse
import json
import re
from typing import Any


UNITS = {
    "": 1,
    "k": 1_000,
    "K": 1_000,
    "w": 10_000,
    "W": 10_000,
    "万": 10_000,
    "m": 1_000_000,
    "M": 1_000_000,
    "亿": 100_000_000,
}

MISSING = {"", "-", "--", "n/a", "na", "null", "none", "未知"}
PATTERN = re.compile(r"^([0-9]+(?:\.[0-9]+)?)\s*([kKwWmM万亿]?)\+?$")


def normalize_metric(value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool):
        raise ValueError("Boolean is not a metric.")
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return round(value)

    raw = str(value).strip().replace(",", "").replace("，", "")
    if raw.lower() in MISSING:
        return None

    match = PATTERN.fullmatch(raw)
    if match is None:
        raise ValueError(f"Unsupported metric format: {value!r}")

    number = float(match.group(1))
    unit = match.group(2)
    return round(number * UNITS[unit])


def self_test() -> None:
    cases = {
        "4.3万": 43_000,
        "2986": 2_986,
        "1.2k": 1_200,
        "2M+": 2_000_000,
        "--": None,
    }
    for raw, expected in cases.items():
        actual = normalize_metric(raw)
        assert actual == expected, (raw, actual, expected)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("values", nargs="*")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("normalize_metrics: ok")
        return 0

    results = []
    for value in args.values:
        try:
            results.append({"raw": value, "normalized": normalize_metric(value)})
        except ValueError as exc:
            results.append({"raw": value, "error": str(exc)})
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

