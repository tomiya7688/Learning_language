from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYGAME_ROOT = ROOT / "教材" / "Python"


@dataclass(frozen=True)
class Violation:
    rule: str
    message: str


RANGES: dict[str, tuple[float, float]] = {
    "player_speed": (1, 10),
    "bullet_speed": (2, 20),
    "enemy_speed": (0.1, 5),
    "enemy_bullet_speed": (1, 12),
    "enemy_fire_interval": (10, 300),
    "player_hp": (1, 10),
    "boss_hp": (5, 500),
    "boss_bullet_speed": (1, 12),
    "boss_fire_interval": (10, 300),
    "boss_bullet_width": (4, 120),
    "boss_bullet_height": (4, 120),
    "player_damage": (1, 50),
}


def find_examples() -> list[Path]:
    return sorted(PYGAME_ROOT.glob("Pg*_*/**/*.py"))


def read_numeric_assignments(path: Path) -> dict[str, float]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    values: dict[str, float] = {}

    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue

        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue

        name = node.targets[0].id

        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, (int, float)):
            values[name] = float(node.value.value)

    return values


def check_values(values: dict[str, float]) -> list[Violation]:
    violations: list[Violation] = []

    for name, (minimum, maximum) in RANGES.items():
        if name not in values:
            continue

        value = values[name]

        if not minimum <= value <= maximum:
            violations.append(
                Violation(
                    f"range:{name}",
                    f"{name}={value:g} は教材用の目安 {minimum:g}〜{maximum:g} を外れています。",
                )
            )

    player_speed = values.get("player_speed")

    if player_speed is not None and player_speed > 0:
        enemy_bullet_speed = values.get("enemy_bullet_speed")

        if enemy_bullet_speed is not None and enemy_bullet_speed > player_speed * 2.2:
            violations.append(
                Violation(
                    "relative:enemy_bullet_speed",
                    (
                        f"enemy_bullet_speed={enemy_bullet_speed:g} が "
                        f"player_speed={player_speed:g} の2.2倍を超えています。"
                    ),
                )
            )

        boss_bullet_speed = values.get("boss_bullet_speed")

        if boss_bullet_speed is not None and boss_bullet_speed > player_speed * 2.4:
            violations.append(
                Violation(
                    "relative:boss_bullet_speed",
                    (
                        f"boss_bullet_speed={boss_bullet_speed:g} が "
                        f"player_speed={player_speed:g} の2.4倍を超えています。"
                    ),
                )
            )

    boss_hp = values.get("boss_hp")
    player_damage = values.get("player_damage")

    if boss_hp is not None and player_damage is not None and player_damage > 0:
        required_hits = boss_hp / player_damage

        if required_hits > 120:
            violations.append(
                Violation(
                    "relative:boss_hits",
                    f"ボス撃破に約{required_hits:.1f}発必要で、教材用の目安120発を超えています。",
                )
            )

    return violations


def is_intentionally_unfair(path: Path) -> bool:
    return path.parent.name.startswith("Pg9_")


def has_oversized_boss_bullet(values: dict[str, float]) -> bool:
    width = values.get("boss_bullet_width")
    height = values.get("boss_bullet_height")

    if width is None or height is None:
        return False

    # 640x480の教材画面で、弾1発が避ける場所を大きく奪うサイズを
    # Pg9の「わざとやらかした状態」とみなす。
    return width >= 320 or height >= 240


def main() -> int:
    examples = find_examples()

    if not examples:
        print("pygameサンプルが見つかりません。")
        return 1

    failed = False

    for path in examples:
        values = read_numeric_assignments(path)
        violations = check_values(values)
        relative = path.relative_to(ROOT)

        if is_intentionally_unfair(path):
            if has_oversized_boss_bullet(values):
                print(f"[PASS: INTENTIONALLY UNFAIR] {relative}")
                print(
                    "  - Pg9のボス弾は、画面を覆って避けにくくなるよう"
                    "意図的に巨大化されています。"
                )
            else:
                print(
                    f"[FAIL] {relative}: Pg9は『ボスの弾がデカすぎる』失敗例なのに、"
                    "boss_bullet_width / boss_bullet_height が十分大きくありません。"
                )
                failed = True
            continue

        if violations:
            print(f"[FAIL] {relative}")
            for violation in violations:
                print(f"  - {violation.message}")
            failed = True
        else:
            checked = ", ".join(
                f"{name}={value:g}"
                for name, value in sorted(values.items())
                if name in RANGES
            )
            print(f"[PASS] {relative}: {checked or '対象パラメータなし'}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
