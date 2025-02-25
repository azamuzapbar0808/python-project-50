from gendiff.scripts.generate_diff import generate_diff

def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read().strip()

def test_generate_diff_json():
    expected_output = read_file('tests/test_data/expected_diff.txt')
    result = generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.json')
    assert result.strip() == expected_output

def test_generate_diff_yaml():
    expected_output = read_file('tests/test_data/expected_diff.txt')
    result = generate_diff('tests/test_data/file1.yml', 'tests/test_data/file2.yml')
    assert result.strip() == expected_output

def test_generate_diff_nested():
    expected_output = read_file('tests/test_data/expected_nested_diff.txt')
    result = generate_diff('tests/test_data/nested1.yml', 'tests/test_data/nested2.yml')
    assert result.strip() == expected_output

def test_generate_diff_plain():
    expected_output = read_file('tests/test_data/expected_plain_diff.txt')
    result = generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.json', 'plain')
    assert result.strip() == expected_output
