import argparse
import json

def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    all_keys = sorted(set(data1.keys()).union(data2.keys()))
    diff = []

    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] != data2[key]:
                diff.append(f'  - {key}: {data1[key]}')
                diff.append(f'  + {key}: {data2[key]}')
        elif key in data1:
            diff.append(f'  - {key}: {data1[key]}')
        elif key in data2:
            diff.append(f'  + {key}: {data2[key]}')

    return '\n'.join(diff)


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')
    parser.add_argument('-f', '--format',
                        choices=['plain', 'json'],
                        default='plain',
                        help='set format of output (default: plain)')
    args = parser.parse_args()

    print(f'Comparing {args.first_file} with {args.second_file}')
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
