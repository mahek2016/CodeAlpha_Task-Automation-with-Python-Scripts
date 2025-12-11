# Email Extractor

A simple Python script that reads a text file, extracts unique email addresses using regex, and writes them to an output file.

## Requirements
- Python 3.8+
- Standard library only (uses `re`, `argparse`, `pathlib`)

## Setup
Place your input file in the project folder (or provide a path).

## Usage
```bash
python main.py --input input.txt --output emails_output.txt --show-count
```
- `--input`: path to the source text file (default: `input.txt`)
- `--output`: path for the extracted emails (default: `emails_output.txt`)
- `--show-count`: optionally print how many unique emails were found

## How it works
1. Reads the input file with UTF-8 encoding (with basic error handling).
2. Uses a compiled regex pattern to find email-like strings.
3. Deduplicates results, sorts them, and writes one email per line to the output file.
4. Optionally prints the total count.

## Files
- `main.py`: main script with CLI entrypoint.
- `input.txt`: sample text with a few emails.
- `emails_output.txt`: generated output after running the script.

## Example
With the provided sample input:
```bash
python main.py --show-count
```
Produces `emails_output.txt` containing the extracted addresses and prints the total found.

