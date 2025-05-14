import json

def export_to_json(data, output_file='output.json'):
    """Export the books data to a JSON file."""
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)
