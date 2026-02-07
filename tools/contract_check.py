from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "examples"

MODE_TOKENS = ("MODE=CLARIFY", "MODE=EXECUTE")


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def check_json_examples() -> None:
    json_files = sorted(EXAMPLES_DIR.glob("**/output/*.json"))
    if not json_files:
        fail("No JSON example outputs found under examples/**/output/*.json")

    for fp in json_files:
        try:
            content = fp.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fail(f"JSON file is not UTF-8 decodable: {fp}")

        try:
            json.loads(content)
        except json.JSONDecodeError as e:
            fail(f"Invalid JSON in {fp}: {e}")

    print(f"OK: JSON examples valid ({len(json_files)} files)")


def check_mode_in_example_inputs() -> None:
    input_files = []
    input_files.extend(EXAMPLES_DIR.glob("**/input/*.txt"))
    input_files.extend(EXAMPLES_DIR.glob("**/input/*.md"))

    if not input_files:
        fail("No example input files found under examples/**/input/*.txt or *.md")

    missing = []
    for fp in sorted(input_files):
        try:
            content = fp.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fail(f"Input file is not UTF-8 decodable: {fp}")

        if not any(tok in content for tok in MODE_TOKENS):
            missing.append(str(fp))

    if missing:
        fail("MODE line missing in example input files:\n- " + "\n- ".join(missing))

    print(f"OK: MODE present in example inputs ({len(input_files)} files)")


def check_markdown_fences() -> None:
    md_files = []
    md_files.extend((ROOT / "system").glob("*.md") if (ROOT / "system").exists() else [])
    md_files.extend((ROOT / "prompts").glob("**/*.md") if (ROOT / "prompts").exists() else [])
    md_files.extend((ROOT / "workflows").glob("*.md") if (ROOT / "workflows").exists() else [])
    md_files.extend((ROOT / "examples").glob("**/*.md") if (ROOT / "examples").exists() else [])
    md_files.extend([ROOT / "README.md"] if (ROOT / "README.md").exists() else [])
    md_files.extend([ROOT / "CHANGELOG.md"] if (ROOT / "CHANGELOG.md").exists() else [])
    md_files.extend([ROOT / "CONTRIBUTING.md"] if (ROOT / "CONTRIBUTING.md").exists() else [])
    md_files = [p for p in md_files if p.exists()]

    bad = []
    for fp in sorted(set(md_files)):
        try:
            content = fp.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fail(f"Markdown file is not UTF-8 decodable: {fp}")

        fence_count = content.count("```")
        if fence_count % 2 != 0:
            bad.append(f"{fp} (``` count={fence_count})")

    if bad:
        fail("Unbalanced markdown code fences detected:\n- " + "\n- ".join(bad))

    print(f"OK: Markdown fences balanced ({len(set(md_files))} files)")


def main() -> None:
    if not EXAMPLES_DIR.exists():
        fail("examples/ directory not found")

    check_json_examples()
    check_mode_in_example_inputs()
    check_markdown_fences()

    print("OK: contract-check passed")


if __name__ == "__main__":
    main()
