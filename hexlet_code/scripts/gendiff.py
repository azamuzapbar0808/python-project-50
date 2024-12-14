import argparse


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
    print(f'Output format: {args.format}')


if __name__ == '__main__':
    main()
