"""
Email extractor script.

Usage:
    python main.py --input input.txt --output emails_output.txt --show-count

Reads a text file, extracts unique email addresses using regex,
and writes them to an output file (one email per line).
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable, Set


EMAIL_PATTERN = re.compile(
    r"""
    [a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+      # local part
    @                                     # at symbol
    [a-zA-Z0-9-]+                         # domain
    (?:\.[a-zA-Z0-9-]+)*                  # optional subdomains
    \.[a-zA-Z]{2,}                        # TLD
    """,
    re.VERBOSE,
)


def read_text_file(path: Path) -> str:
    """Read text content from a file with basic error handling."""
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise SystemExit(f"Input file not found: {path}") from exc
    except OSError as exc:
        raise SystemExit(f"Could not read file {path}: {exc}") from exc


def extract_emails(text: str) -> Set[str]:
    """Return a set of unique emails found in the provided text."""
    return set(match.group(0) for match in EMAIL_PATTERN.finditer(text))


def write_emails(path: Path, emails: Iterable[str]) -> None:
    """Write emails (one per line) to the output file."""
    try:
        path.write_text("\n".join(sorted(emails)), encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"Could not write output file {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract unique emails from a text file.")
    parser.add_argument("--input", default="input.txt", help="Path to input text file.")
    parser.add_argument(
        "--output",
        default="emails_output.txt",
        help="Path to save extracted emails (one per line).",
    )
    parser.add_argument(
        "--show-count",
        action="store_true",
        help="Print how many unique emails were extracted.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    text = read_text_file(input_path)
    emails = extract_emails(text)
    write_emails(output_path, emails)

    if args.show_count:
        print(f"Extracted {len(emails)} unique email(s). Output: {output_path}")


if __name__ == "__main__":
    main()

