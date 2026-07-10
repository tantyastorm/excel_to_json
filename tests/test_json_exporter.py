import json

from processor.json_exporter import export_json


def test_export_json_creates_file(tmp_path):
    output_file = tmp_path / "output.json"
    data = [{"Title": "Book A", "Price": 10}]
    export_json(data, str(output_file))
    assert output_file.exists()
    with output_file.open("r", encoding="utf-8") as f:
        loaded = json.load(f)
    assert loaded == data


def test_export_json_creates_parent_directories(tmp_path):
    output_file = tmp_path / "nested" / "exports" / "output.json"
    data = [{"Title": "Book A"}]
    export_json(data, str(output_file))
    assert output_file.exists()
    with output_file.open("r", encoding="utf-8") as f:
        assert json.load(f) == data
