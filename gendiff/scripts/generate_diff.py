import yaml


def load_yaml(filepath):
    """Загружает YAML файл."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def generate_diff(file_path1, file_path2):
    """Генерирует различия между двумя YAML файлами."""
    data1 = load_yaml(file_path1)
    data2 = load_yaml(file_path2)

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

    # Приводим булевые значения к маленьким буквам
    diff_result = [line.replace('True', 'true').replace('False', 'false') for line in diff_result]

    return "{\n" + "\n".join(diff_result) + "\n}"
