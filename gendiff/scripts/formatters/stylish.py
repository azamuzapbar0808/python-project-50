def format_stylish(diff, depth=0):
    indent = " " * (depth * 4)
    result = ["{"]

    for key, value in diff.items():
        status = value["status"]

        if status == "removed":
            result.append(f"{indent}  - {key}: {format_value(value['value'], depth + 1)}")
        elif status == "added":
            result.append(f"{indent}  + {key}: {format_value(value['value'], depth + 1)}")
        elif status == "changed":
            result.append(f"{indent}  - {key}: {format_value(value['old_value'], depth + 1)}")
            result.append(f"{indent}  + {key}: {format_value(value['new_value'], depth + 1)}")
        elif status == "unchanged":
            result.append(f"{indent}    {key}: {format_value(value['value'], depth + 1)}")
        elif status == "nested":
            nested_output = format_stylish(value["children"], depth + 1)
            result.append(f"{indent}    {key}: {nested_output}")

    result.append(indent + "}")
    return "\n".join(result)


def format_value(value, depth):
    if isinstance(value, dict):
        indent = " " * (depth * 4)
        lines = ["{"]
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {format_value(v, depth + 1)}")
        lines.append(indent + "}")
        return "\n".join(lines)
    return str(value)
