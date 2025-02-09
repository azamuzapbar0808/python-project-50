#!/usr/bin/env python3

import argparse
import json

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")

    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        default="plain"
    )

    args = parser.parse_args()

    file1_data = load_json(args.first_file)
    file2_data = load_json(args.second_file)

    print(f"Comparing {args.first_file} with {args.second_file} in {args.format} format.")
    print("File 1 content:", file1_data)
    print("File 2 content:", file2_data)

if __name__ == "__main__":
    main()
