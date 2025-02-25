import json
import yaml
from gendiff.scripts.formatters.json import format_json
from gendiff.scripts.formatters.stylish import format_stylish


def parse_file(filepath):
    if filepath.endswith(".json"):
        with open(filepath) as f:
            return json.load(f)
    elif filepath.endswith(".yml") or filepath.endswith(".yaml"):
        with open(filepath) as f:
            return yaml.safe_load(f)
    else:
        raise ValueError("Unsupported file format")


def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = {}

    for key in keys:
        if key in data1 and key not in data2:
            diff[key] = {"status": "removed", "value": data1[key]}
        elif key not in data1 and key in data2:
            diff[key] = {"status": "added", "value": data2[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {"status": "nested", "children": build_diff(data1[key], data2[key])}
        elif data1[key] != data2[key]:
            diff[key] = {"status": "changed", "old_value": data1[key], "new_value": data2[key]}
        else:
            diff[key] = {"status": "unchanged", "value": data1[key]}

    return diff


def generate_diff(file1, file2, format_name="stylish"):
    data1 = parse_file(file1)
    data2 = parse_file(file2)
    diff = build_diff(data1, data2)

    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        from gendiff.scripts.formatters.plain import format_plain
        return format_plain(diff)
    elif format_name == "json":
        return format_json(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")
