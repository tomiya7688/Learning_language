"""Format only explicitly selected Python files with the pinned Ruff version."""

import argparse
from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()
    pin = (
        (root / "requirements-dev.txt")
        .read_text(encoding="utf-8")
        .strip()
        .split("==")[1]
    )
    version = subprocess.check_output(
        [sys.executable, "-m", "ruff", "--version"], text=True
    ).strip()
    if version != f"ruff {pin}":
        raise SystemExit("Run: python -m pip install -r requirements-dev.txt")
    paths = args.paths or [
        "tools/format.py",
        "教材/Python/基礎編_ゆっくり学びたい人へ/教材/08_クラス/student_class.py",
    ]
    targets = []
    for item in paths:
        target = (root / item).resolve(strict=True)
        if not target.is_relative_to(root) or target.suffix != ".py":
            raise SystemExit(
                f"Target must be a Python file inside this checkout: {item}"
            )
        targets.append(str(target))
    command = [
        sys.executable,
        "-m",
        "ruff",
        "format",
        "--config",
        str(root / "pyproject.toml"),
    ]
    if args.check:
        command.append("--check")
    raise SystemExit(subprocess.call(command + targets))


if __name__ == "__main__":
    main()
