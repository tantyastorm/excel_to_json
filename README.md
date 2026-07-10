# Smart Excel to JSON Exporter

## Overview

Smart Excel to JSON Exporter is a small Python CLI utility that converts selected columns from a `.xlsx` workbook into formatted JSON. It is intended for simple local data cleanup and export tasks, not as a full Excel automation platform.

## Features

- Loads `.xlsx` workbooks with pandas and openpyxl
- Displays available workbook headers before export
- Lets the user choose which columns to include
- Trims whitespace, ignores empty selections, and removes duplicate field selections
- Validates selected fields before exporting
- Writes formatted JSON to a default or custom output path
- Includes focused pytest coverage

## Tech Stack

- Python
- pandas
- openpyxl
- pytest

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

On macOS or Linux, activate the environment with:

```bash
source .venv/bin/activate
```

## Usage

```bash
python main.py --file sample_data/test.xlsx --output output/books_output.json
```

The tool prints the available headers and prompts for comma-separated fields:

```text
Available headers: ['title', 'price', 'stock', 'image_url']
Enter the headers to extract (comma-separated): title, price, stock
Exported data to output/books_output.json
```

If `--output` is omitted, the tool writes to `output.json`.

## Example Output

```json
[
    {
        "title": "A Light in the Attic",
        "price": 51.77,
        "stock": "In stock"
    }
]
```

## Supported Input Format

Input files must be `.xlsx` workbooks with a header row. The current workflow exports row-based records, where each worksheet row becomes one JSON object.

The included sample files use public demo book data from Books to Scrape.

## Limitations

- Supports `.xlsx` only
- Reads the default worksheet only
- Exports row-based records only
- Does not provide a GUI
- Does not transform or normalize values beyond selecting columns

## Privacy

Processing is local. The tool does not upload workbook data, call external APIs, or store credentials.

## Project Status

This is a compact portfolio project demonstrating a practical Python data-export workflow. It is intentionally small and focused.
