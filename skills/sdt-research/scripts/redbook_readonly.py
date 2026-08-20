#!/usr/bin/env python3
"""Run an allow-listed, read-only Redbook CLI command."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path


ALLOWED = {
    "whoami",
    "search",
    "user",
    "user-posts",
    "read",
    "comments",
    "analyze-viral",
    "viral-template",
    "topics",
}

BLOCKED_FLAGS = {
    "--cookie",
    "--cookies",
    "--token",
    "--xsec-token",
    "--xsec_token",
}

DETAIL_COMMANDS = {
    "user",
    "user-posts",
    "read",
    "comments",
    "analyze-viral",
    "viral-template",
}

STOP_MARKERS = (
    "needverify",
    "captcha",
    "verification required",
    "session expired",
    "login expired",
    "登录已过期",
    "验证码",
    "访问频繁",
    "操作频繁",
    "ip blocked",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Execute one allow-listed read-only Redbook command."
    )
    parser.add_argument(
        "--detail-delay-seconds",
        type=float,
        default=1.5,
        help="Delay before detail commands; clamped to 1–10 seconds.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=45,
        help="Command timeout; clamped to 5–60 seconds.",
    )
    parser.add_argument(
        "redbook_args",
        nargs=argparse.REMAINDER,
        help="Redbook command and arguments, for example: search 茶室",
    )
    return parser.parse_args()


def validate(redbook_args: list[str]) -> str:
    if not redbook_args:
        raise ValueError("Missing Redbook command.")

    command = redbook_args[0].lower()
    if command not in ALLOWED:
        allowed = ", ".join(sorted(ALLOWED))
        raise ValueError(
            f"Blocked command: {command!r}. Allowed read-only commands: {allowed}"
        )

    lowered = {arg.lower().split("=", 1)[0] for arg in redbook_args[1:]}
    blocked = lowered.intersection(BLOCKED_FLAGS)
    if blocked:
        raise ValueError(
            "Credential flags are blocked: " + ", ".join(sorted(blocked))
        )
    return command


def main() -> int:
    args = parse_args()
    try:
        command = validate(args.redbook_args)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    user_runtime = Path("/Users/ineveron/.local/share/sdt-runtime")
    node_bin = user_runtime / "node" / "current" / "bin"
    redbook_bin = user_runtime / "redbook" / "bin"
    search_path = os.pathsep.join(
        [str(node_bin), str(redbook_bin), os.environ.get("PATH", "")]
    )
    binary = shutil.which("redbook", path=search_path)
    if binary is None:
        print(
            "ERROR: Redbook CLI is not installed or is not on PATH. "
            "Install @lucasygu/redbook only after user approval.",
            file=sys.stderr,
        )
        return 127

    if command in DETAIL_COMMANDS:
        delay = min(10.0, max(1.0, args.detail_delay_seconds))
        time.sleep(delay)

    timeout = min(60, max(5, args.timeout_seconds))
    try:
        runtime_env = os.environ.copy()
        runtime_env["PATH"] = search_path
        completed = subprocess.run(
            [binary, *args.redbook_args],
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=runtime_env,
        )
    except subprocess.TimeoutExpired:
        print(
            "STOP: Redbook command timed out. No automatic retry was attempted.",
            file=sys.stderr,
        )
        return 124

    if completed.stdout:
        sys.stdout.write(completed.stdout)
    if completed.stderr:
        sys.stderr.write(completed.stderr)

    combined = f"{completed.stdout}\n{completed.stderr}".lower()
    if any(marker in combined for marker in STOP_MARKERS):
        print(
            "\nSTOP: Verification, expiry, or rate-limit signal detected. "
            "Do not retry automatically.",
            file=sys.stderr,
        )
        return 3

    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
