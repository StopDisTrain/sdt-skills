#!/usr/bin/env python3
"""Score SDT topic candidates from a JSON document."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


POSITIVE_LIMITS = {
    "account_fit": 20,
    "product_bridge": 20,
    "source_evidence": 15,
    "mechanism_clarity": 15,
    "audience_motivation": 10,
    "packaging_potential": 10,
    "production_feasibility": 10,
}

PENALTIES = {
    "forced_product": 20,
    "stale_trend": 10,
    "one_off_sample": 10,
    "unsupported_claim": 20,
}

HARD_REJECTS = {
    "fabricated_persona",
    "noun_swap_copy",
}


def bounded_score(topic: dict[str, Any], field: str, limit: int) -> int:
    value = topic.get(field, 0)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number")
    if value < 0 or value > limit:
        raise ValueError(f"{field} must be between 0 and {limit}")
    return round(value)


def decision(total: int, rejected: bool) -> str:
    if rejected:
        return "rejected"
    if total >= 80:
        return "priority"
    if total >= 70:
        return "revise"
    if total >= 60:
        return "research-only"
    return "drop"


def score_topic(topic: dict[str, Any]) -> dict[str, Any]:
    breakdown = {
        field: bounded_score(topic, field, limit)
        for field, limit in POSITIVE_LIMITS.items()
    }
    gross = sum(breakdown.values())

    flags = topic.get("penalties", {})
    if not isinstance(flags, dict):
        raise ValueError("penalties must be an object")

    hard_reasons = sorted(
        field for field in HARD_REJECTS if bool(flags.get(field, False))
    )
    applied_penalties = {
        field: points
        for field, points in PENALTIES.items()
        if bool(flags.get(field, False))
    }
    total = max(0, gross - sum(applied_penalties.values()))
    rejected = bool(hard_reasons)

    result = dict(topic)
    result["score_breakdown"] = breakdown
    result["gross_score"] = gross
    result["applied_penalties"] = applied_penalties
    result["hard_reject_reasons"] = hard_reasons
    result["total_score"] = total
    result["decision"] = decision(total, rejected)
    return result


def load_topics(path: str) -> list[dict[str, Any]]:
    if path == "-":
        payload = json.load(sys.stdin)
    else:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    topics = payload.get("topics") if isinstance(payload, dict) else payload
    if not isinstance(topics, list) or not all(isinstance(x, dict) for x in topics):
        raise ValueError("Input must be a JSON array or an object with a topics array.")
    return topics


def self_test() -> None:
    sample = {
        "topic_id": "sample",
        "account_fit": 18,
        "product_bridge": 17,
        "source_evidence": 13,
        "mechanism_clarity": 14,
        "audience_motivation": 9,
        "packaging_potential": 8,
        "production_feasibility": 9,
        "penalties": {"stale_trend": True},
    }
    scored = score_topic(sample)
    assert scored["gross_score"] == 88
    assert scored["total_score"] == 78
    assert scored["decision"] == "revise"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", help="JSON file path, or - for stdin")
    parser.add_argument("--top", type=int, default=0)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("score_topics: ok")
        return 0
    if not args.input:
        parser.error("input is required unless --self-test is used")

    try:
        scored = [score_topic(topic) for topic in load_topics(args.input)]
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    scored.sort(
        key=lambda item: (
            item["decision"] == "rejected",
            -item["total_score"],
            str(item.get("topic_id", "")),
        )
    )
    if args.top > 0:
        scored = scored[: args.top]
    print(json.dumps({"topics": scored}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

