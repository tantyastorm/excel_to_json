import pytest
from utils.file_loader import load_excel_file

def test_invalid_file_extension():
    with pytest.raises(ValueError):
        load_excel_file("sample_data/test.txt")

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_excel_file("nonexistent.xlsx")
