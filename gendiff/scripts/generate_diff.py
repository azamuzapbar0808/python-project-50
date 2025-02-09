import json


def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def generate_diff(file_path1, file_path2):
    data1 = load_json(file_path1)
    data2 = load_json(file_path2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_result = []

    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff_result.append(f"    {key}: {data1[key]}")
            else:
                diff_result.append(f"  - {key}: {data1[key]}")
                diff_result.append(f"  + {key}: {data2[key]}")
        elif key in data1:
            diff_result.append(f"  - {key}: {data1[key]}")
        else:
            diff_result.append(f"  + {key}: {data2[key]}")

    return "{\n" + "\n".join(diff_result) + "\n}"
