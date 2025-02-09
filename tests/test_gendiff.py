from gendiff import generate_diff

def test_generate_diff():
    result = generate_diff("tests/test_data/file1.json", "tests/test_data/file2.json")
    expected = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
    assert result.strip() == expected.strip()
