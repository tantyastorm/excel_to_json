import json
from pathlib import Path

def export_json(data, filename="output.json"):
    output_path = Path(filename)
    if output_path.parent != Path("."):
        output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except OSError as exc:
        raise OSError(f"Could not write output file '{output_path}': {exc}") from exc
    print(f"Exported data to {filename}")
