import json


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def main():
    file1_path = 'hexlet_code/scripts/file1.json'
    file2_path = 'hexlet_code/scripts/file2.json'

    data1 = read_json(file1_path)
    data2 = read_json(file2_path)

    print("Data from file1:", data1)
    print("Data from file2:", data2)


if __name__ == "__main__":
    main()
