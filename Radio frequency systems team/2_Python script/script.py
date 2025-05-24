#!/usr/bin/env python3

import sys, re, os

def main():
    if len(sys.argv) != 3:
        sys.stderr.write(f"Usage: {sys.argv[0]} <file> <search_pattern>\n")
        sys.exit(1)

    filename, pattern = sys.argv[1], sys.argv[2]

    if not os.path.isfile(filename) or not os.access(filename, os.R_OK):
        sys.stderr.write(f"Error: cannot read file '{filename}'\n")
        sys.exit(2)

    try:
        regex = re.compile(pattern, re.IGNORECASE)
    except re.error as e:
        sys.stderr.write(f"Invalid pattern '{pattern}': {e}\n")
        sys.exit(3)

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if regex.search(line):
                print(line.rstrip())

if __name__ == "__main__":
    main()
