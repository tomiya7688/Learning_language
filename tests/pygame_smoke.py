from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYGAME_ROOT = ROOT / "教材" / "Python"
STARTUP_SECONDS = 1.5


def find_examples() -> list[Path]:
    return sorted(PYGAME_ROOT.glob("Pg*_*/**/*.py"))


def run_example(path: Path) -> tuple[bool, str]:
    env = os.environ.copy()
    env["SDL_VIDEODRIVER"] = "dummy"
    env["SDL_AUDIODRIVER"] = "dummy"
    env["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

    process = subprocess.Popen(
        [sys.executable, path.name],
        cwd=path.parent,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    deadline = time.monotonic() + STARTUP_SECONDS

    while time.monotonic() < deadline:
        return_code = process.poll()

        if return_code is not None:
            output = process.stdout.read() if process.stdout else ""

            if return_code == 0:
                return True, "正常終了"

            return False, output.strip() or f"exit code {return_code}"

        time.sleep(0.05)

    process.terminate()

    try:
        process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=2)

    return True, f"{STARTUP_SECONDS}秒以上正常に実行"


def main() -> int:
    examples = find_examples()

    if not examples:
        print("pygameサンプルが見つかりません。")
        return 1

    failed = False

    for path in examples:
        ok, message = run_example(path)
        relative = path.relative_to(ROOT)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {relative}: {message}")

        if not ok:
            failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
