import json
import subprocess
import sys

import pandas as pd


def create_workbook(path):
    pd.DataFrame({
        "title": ["Book A", "Book B"],
        "price": [10.5, 12.0],
        "stock": ["In stock", "Out of stock"],
    }).to_excel(path, index=False)


def test_cli_conversion_with_custom_output_path(tmp_path):
    workbook = tmp_path / "books.xlsx"
    output = tmp_path / "nested" / "books.json"
    create_workbook(workbook)

    result = subprocess.run(
        [
            sys.executable,
            "main.py",
            "--file",
            str(workbook),
            "--output",
            str(output),
        ],
        input="title, price\n",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0
    assert "Available headers:" in result.stdout
    assert "Exported data to" in result.stdout
    assert output.exists()
    with output.open("r", encoding="utf-8") as f:
        assert json.load(f) == [
            {"title": "Book A", "price": 10.5},
            {"title": "Book B", "price": 12.0},
        ]


def test_cli_returns_non_zero_for_invalid_input(tmp_path):
    workbook = tmp_path / "books.txt"
    workbook.write_text("not an xlsx file", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, "main.py", "--file", str(workbook)],
        input="title\n",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode != 0
    assert "Error: Only .xlsx files are supported" in result.stderr
