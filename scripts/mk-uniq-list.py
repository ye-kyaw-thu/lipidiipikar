"""
Removing 1st character from both of the columns. Sorting, Unique feature also supported.
Written by Ye Kyaw Thu, LU Lab., Myanmar
Last updated: 30 Dec 2024

How to run:
python ./mk-uniq-list.py --input ./tst-data/manual-conv.txt --output ./manual-conv.clean
python ./mk-uniq-list.py --input ./tst-data/manual-conv.txt --output ./manual-conv.clean --sort
python ./mk-uniq-list.py --input ./tst-data/manual-conv.txt --output ./manual-conv.clean --uniq
"""

import argparse
import sys

def process_file(input_file, output_file=None, sort=False, uniq=False):
    # Read lines from input file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Process lines by removing the first character from both columns
    processed_lines = []
    for line in lines:
        if '\t' in line:
            col1, col2 = line.split('\t', 1)
            processed_lines.append((col1[1:], col2[1:]))

    # If sorting is enabled
    if sort:
        processed_lines.sort(key=lambda x: x[0])

    # If unique is enabled
    if uniq:
        processed_lines = list(dict.fromkeys(processed_lines))

    # Prepare output lines
    output_lines = ['\t'.join(pair) for pair in processed_lines]

    # Write to the output file or print to stdout
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_lines) + '\n')
    else:
        print('\n'.join(output_lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a two-column file by removing the first character from each column.")
    parser.add_argument("--input", required=True, help="Input file name.")
    parser.add_argument("--output", help="Output file name. If not specified, results will be printed to stdout.")
    parser.add_argument("--sort", action="store_true", help="Sort the output by the first column.")
    parser.add_argument("--uniq", action="store_true", help="Sort by the first column and make the list unique.")

    args = parser.parse_args()

    try:
        process_file(args.input, args.output, args.sort, args.uniq)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

