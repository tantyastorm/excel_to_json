import os
import json
from processor.json_exporter import export_json

def test_export_json_creates_file(tmp_path):
    output_file = tmp_path / "output.json"
    data = [{"Title": "Book A", "Price": 10}]
    export_json(data, str(output_file))
    assert os.path.exists(output_file)
    with open(output_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    assert loaded == data
