def format_plain(diff, path=""):
    lines = []

    for key, value in sorted(diff.items()):
        full_path = f"{path}.{key}".lstrip(".")
        status = value["status"]

        if status == "added":
            formatted_value = format_value(value["value"])
            lines.append(f"Property '{full_path}' was added with value: {formatted_value}")
        elif status == "removed":
            lines.append(f"Property '{full_path}' was removed")
        elif status == "changed":
            old_value = format_value(value["old_value"])
            new_value = format_value(value["new_value"])
            lines.append(f"Property '{full_path}' was updated. From {old_value} to {new_value}")
        elif status == "nested":
            lines.append(format_plain(value["children"], full_path))

    return "\n".join(filter(None, lines))


def format_value(value):
    if isinstance(value, dict) or isinstance(value, list):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    return str(value)
