"""Rust教材のファイルとMarkdownリンクの簡単な回帰チェック。"""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
RUST = ROOT / "教材" / "Rust"
LESSONS = RUST / "教材"


class TestRustCurriculum(unittest.TestCase):
    def test_all_24_chapters_exist(self):
        for number in range(24):
            pages = list(LESSONS.glob(f"{number:02d}_*.md"))
            self.assertEqual(1, len(pages), f"章{number:02d}のページ数")

    def test_local_markdown_links_exist(self):
        for page in RUST.rglob("*.md"):
            with self.subTest(page=page.relative_to(ROOT)):
                content = page.read_text(encoding="utf-8")
                for target in re.findall(r"\]\(([^)]+)\)", content):
                    if target.startswith(("https://", "http://", "#", "mailto:")):
                        continue
                    file_path = target.split("#", 1)[0]
                    if not file_path:
                        continue
                    resolved = (page.parent / file_path).resolve()
                    self.assertTrue(resolved.is_relative_to(ROOT))
                    self.assertTrue(resolved.exists(), f"{page}: {target}")

    def test_each_runnable_chapter_has_source(self):
        for number in range(2, 24):
            page = next(LESSONS.glob(f"{number:02d}_*.md"))
            text = page.read_text(encoding="utf-8")
            self.assertIn("cargo run --example", text, str(page))
            self.assertIn("## 変更して試す", text, str(page))
            self.assertIn("## コードの読み方", text, str(page))

    def test_readme_links_to_rust(self):
        self.assertIn("[Rust](./Rust/初めに.md)", (ROOT / "教材" / "教材一覧.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
