from gendiff.scripts import generate_diff


def test_generate_diff():
    result = generate_diff.generate_diff("tests/test_data/file1.yml",
                                         "tests/test_data/file2.yml")
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert result.strip() == expected.strip()
