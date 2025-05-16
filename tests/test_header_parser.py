import pandas as pd
from processor.header_parser import get_headers

def test_get_headers_row(monkeypatch):
    df = pd.DataFrame({
        "Title": ["Book A"],
        "Price": [10],
        "Stock": [5]
    })
    monkeypatch.setattr("builtins.input", lambda _: "Title,Price")
    headers = get_headers(df, "row")
    assert headers == ["Title", "Price"]
