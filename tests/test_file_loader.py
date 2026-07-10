import pandas as pd
import pytest

from utils.file_loader import load_excel_file


@pytest.fixture
def workbook_path(tmp_path):
    path = tmp_path / "books.xlsx"
    pd.DataFrame({
        "title": ["Book A"],
        "price": [10.5],
        "stock": ["In stock"],
    }).to_excel(path, index=False)
    return path


def test_valid_xlsx_loading(workbook_path):
    df = load_excel_file(str(workbook_path))
    assert df.to_dict(orient="records") == [
        {"title": "Book A", "price": 10.5, "stock": "In stock"}
    ]


def test_invalid_file_extension():
    with pytest.raises(ValueError, match="Only .xlsx files are supported"):
        load_excel_file("sample_data/test.txt")


def test_unreadable_workbook(tmp_path):
    workbook = tmp_path / "broken.xlsx"
    workbook.write_text("not a real workbook", encoding="utf-8")
    with pytest.raises(ValueError, match="Could not read workbook"):
        load_excel_file(str(workbook))


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_excel_file("nonexistent.xlsx")
