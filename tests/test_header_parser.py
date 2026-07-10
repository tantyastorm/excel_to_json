import pandas as pd
import pytest

from processor.header_parser import get_headers, parse_headers, validate_headers


def test_get_headers_row(monkeypatch):
    df = pd.DataFrame({
        "Title": ["Book A"],
        "Price": [10],
        "Stock": [5],
    })
    monkeypatch.setattr("builtins.input", lambda _: "Title,Price")
    headers = get_headers(df)
    assert headers == ["Title", "Price"]


def test_header_trimming():
    assert parse_headers(" Title , Price ") == ["Title", "Price"]


def test_empty_values_are_ignored():
    assert parse_headers("Title,, ,Price") == ["Title", "Price"]


def test_duplicate_selected_headers_are_removed():
    assert parse_headers("Title,Price,Title, Stock, Price") == ["Title", "Price", "Stock"]


def test_empty_selection_is_rejected():
    with pytest.raises(ValueError, match="Select at least one field"):
        parse_headers(" , , ")


def test_invalid_headers_are_rejected():
    with pytest.raises(ValueError) as exc_info:
        validate_headers(["Title", "Missing"], ["Title", "Price"])
    message = str(exc_info.value)
    assert "Invalid field(s): Missing" in message
    assert "Available fields: Title, Price" in message
