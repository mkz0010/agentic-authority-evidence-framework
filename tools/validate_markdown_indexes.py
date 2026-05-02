#!/usr/bin/env python3
"""
Validate Markdown index and navigation documents.

Purpose:
    This script is a lightweight quality gate for repository navigation
    documents. It is intentionally narrower than a full Markdown linter.

    It catches issues that are easy to miss in normal artifact validators,
    including:
    - malformed rows in docs/en/document-map.md tables;
    - broken file paths listed in docs/en/document-map.md;
    - duplicate document-map path rows;
    - malformed docs/en/status/README.md status index entries;
    - missing or extra status document index entries;
    - placeholder table rows left in tables that already contain real entries.

Exit code:
    0 if validation passes.
    1 if one or more validation errors are found.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCUMENT_MAP = REPO_ROOT / "docs" / "en" / "document-map.md"
STATUS_README = REPO_ROOT / "docs" / "en" / "status" / "README.md"
STATUS_DIR = REPO_ROOT / "docs" / "en" / "status"

DOC_MAP_PATH_CELL_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|")
STATUS_README_LINK_RE = re.compile(
    r"^- \[`(?P<label>[^`]+)`\]\((?P<target>[^)]+)\)\s+[—-]\s+(?P<description>.+?)\.?$"
)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def read_lines(path: Path, errors: list[str]) -> list[str]:
    if not path.exists():
        errors.append(f"Missing required file: {rel(path)}")
        return []
    return path.read_text(encoding="utf-8").splitlines()


def validate_document_map(errors: list[str]) -> None:
    lines = read_lines(DOCUMENT_MAP, errors)
    if not lines:
        return

    seen_paths: dict[str, int] = {}

    for line_no, line in enumerate(lines, start=1):
        if not line.startswith("|"):
            continue

        # All tables in document-map.md are expected to have three columns.
        if line.count("|") != 4:
            errors.append(
                f"{rel(DOCUMENT_MAP)}:{line_no}: table row does not have exactly "
                f"3 columns: {line}"
            )
            continue

        match = DOC_MAP_PATH_CELL_RE.match(line)
        if not match:
            continue

        listed_path = match.group(1)
        candidate = REPO_ROOT / listed_path

        if not candidate.exists():
            errors.append(
                f"{rel(DOCUMENT_MAP)}:{line_no}: listed path does not exist: "
                f"{listed_path}"
            )

        if listed_path in seen_paths:
            errors.append(
                f"{rel(DOCUMENT_MAP)}:{line_no}: duplicate path entry "
                f"'{listed_path}' first listed on line {seen_paths[listed_path]}."
            )
        else:
            seen_paths[listed_path] = line_no

    validate_placeholder_rows(DOCUMENT_MAP, lines, errors)


def validate_placeholder_rows(path: Path, lines: list[str], errors: list[str]) -> None:
    """Reject placeholder rows inside tables that also contain real path rows."""

    table: list[tuple[int, str]] = []

    def flush_table() -> None:
        if not table:
            return

        has_placeholder = any("_No matching documents in this category yet._" in row for _, row in table)
        has_real_path_row = any(re.match(r"^\|\s*`[^`]+`\s*\|", row) for _, row in table)

        if has_placeholder and has_real_path_row:
            placeholder_lines = [
                str(line_no)
                for line_no, row in table
                if "_No matching documents in this category yet._" in row
            ]
            errors.append(
                f"{rel(path)}:{','.join(placeholder_lines)}: placeholder row appears "
                "in a table that already contains real path entries."
            )

    for line_no, line in enumerate(lines, start=1):
        if line.startswith("|"):
            table.append((line_no, line))
            continue

        flush_table()
        table = []

    flush_table()


def validate_status_readme(errors: list[str]) -> None:
    lines = read_lines(STATUS_README, errors)
    if not lines:
        return

    try:
        start = next(
            i for i, line in enumerate(lines)
            if line.strip() == "## Current Status Documents"
        )
    except StopIteration:
        errors.append(f"{rel(STATUS_README)}: missing '## Current Status Documents' section.")
        return

    end = len(lines)
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("## "):
            end = i
            break

    listed_targets: dict[str, int] = {}

    for line_no, line in enumerate(lines[start + 1:end], start=start + 2):
        if not line.strip():
            continue

        if not line.startswith("- "):
            errors.append(
                f"{rel(STATUS_README)}:{line_no}: expected bullet list entry: {line}"
            )
            continue

        match = STATUS_README_LINK_RE.match(line)
        if not match:
            errors.append(
                f"{rel(STATUS_README)}:{line_no}: malformed status index entry: {line}"
            )
            continue

        label = match.group("label")
        target = match.group("target")

        if "/" in target or target.startswith("."):
            errors.append(
                f"{rel(STATUS_README)}:{line_no}: status README target should be a "
                f"local filename, got: {target}"
            )
            continue

        if label != f"docs/en/status/{target}":
            errors.append(
                f"{rel(STATUS_README)}:{line_no}: link label and target disagree: "
                f"label '{label}', target '{target}'."
            )

        target_path = STATUS_README.parent / target
        if not target_path.exists():
            errors.append(
                f"{rel(STATUS_README)}:{line_no}: linked status document does not exist: "
                f"{target}"
            )

        if target in listed_targets:
            errors.append(
                f"{rel(STATUS_README)}:{line_no}: duplicate status README entry "
                f"'{target}' first listed on line {listed_targets[target]}."
            )
        else:
            listed_targets[target] = line_no

    actual_status_docs = {
        path.name
        for path in STATUS_DIR.glob("*.md")
        if path.name != "README.md"
    }

    listed = set(listed_targets)

    missing = sorted(actual_status_docs - listed)
    extra = sorted(listed - actual_status_docs)

    for name in missing:
        errors.append(
            f"{rel(STATUS_README)}: missing status README entry for docs/en/status/{name}."
        )

    for name in extra:
        errors.append(
            f"{rel(STATUS_README)}: status README lists non-status document: {name}."
        )


def validate_document_map_status_coverage(errors: list[str]) -> None:
    lines = read_lines(DOCUMENT_MAP, errors)
    if not lines:
        return

    listed_status_docs: set[str] = set()
    for line in lines:
        match = DOC_MAP_PATH_CELL_RE.match(line)
        if not match:
            continue
        path = match.group(1)
        if path.startswith("docs/en/status/") and path.endswith(".md"):
            listed_status_docs.add(Path(path).name)

    actual_status_docs = {
        path.name
        for path in STATUS_DIR.glob("*.md")
        if path.name != "README.md"
    }

    missing = sorted(actual_status_docs - listed_status_docs)
    extra = sorted(listed_status_docs - actual_status_docs)

    for name in missing:
        errors.append(
            f"{rel(DOCUMENT_MAP)}: missing document-map row for docs/en/status/{name}."
        )

    for name in extra:
        errors.append(
            f"{rel(DOCUMENT_MAP)}: document-map lists non-status document: {name}."
        )



def validate_numbered_docs_registered(errors: list[str]) -> None:
    """Ensure top-level numbered docs/en/*.md files are listed in document-map.md."""
    document_map_text = DOCUMENT_MAP.read_text(encoding="utf-8")
    registered_paths = set(
        re.findall(r"`(docs/en/[^`]+\.md)`", document_map_text)
    )

    numbered_doc_pattern = re.compile(r"^\d{2}-.*\.md$")
    numbered_docs = sorted(
        path
        for path in (REPO_ROOT / "docs" / "en").glob("*.md")
        if numbered_doc_pattern.match(path.name)
    )

    for numbered_doc in numbered_docs:
        expected = f"docs/en/{numbered_doc.name}"
        if expected not in registered_paths:
            errors.append(
                f"{rel(DOCUMENT_MAP)}: missing document-map row for numbered document {expected}."
            )


def main() -> int:
    errors: list[str] = []

    validate_document_map(errors)
    validate_numbered_docs_registered(errors)
    validate_status_readme(errors)
    validate_document_map_status_coverage(errors)

    if errors:
        print("ERROR: Markdown index validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: Markdown indexes validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
