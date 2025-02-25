#!/usr/bin/env python3

import argparse
from gendiff.scripts.generate_diff import generate_diff

def parse_arguments():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", type=str, help="Path to the first file")
    parser.add_argument("second_file", type=str, help="Path to the second file")
    parser.add_argument("-f", "--format", choices=["stylish", "plain", "json"], default="stylish",
                        help="Set output format")
    return parser.parse_args()

def main():
    args = parse_arguments()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)

if __name__ == "__main__":
    main()
