"""
Converting tab two columns format to json.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 30 Dec 2024.

How to run: 
python ../tab2json.py --input ./manual-conv-without-athat.uniq --output ./manual-conv-without-athat.uniq.json
python ../tab2json.py --input ./manual-conv-without-athat.uniq --output ./manual-conv-without-athat.uniq.json --sort desc

"""

import argparse
import sys
import json

def convert_to_dict(input_file, output_file=None, sort=None):
    # Read lines from input file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Convert lines to dictionary format
    result_dict = {}
    for line in lines:
        if '\t' in line:
            key, value = line.split('\t', 1)
            result_dict[key] = value

    # Sort the dictionary if sorting is enabled
    if sort:
        reverse = sort == "desc"
        sorted_items = sorted(result_dict.items(), key=lambda x: len(x[0]), reverse=reverse)
        result_dict = dict(sorted_items)

    # Convert dictionary to JSON string
    json_output = json.dumps(result_dict, ensure_ascii=False, indent=4)

    # Write to output file or print to stdout
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(json_output + '\n')
    else:
        print(json_output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a two-column file to JSON dictionary format.")
    parser.add_argument("--input", required=True, help="Input file name.")
    parser.add_argument("--output", help="Output file name. If not specified, results will be printed to stdout.")
    parser.add_argument("--sort", choices=["asc", "desc"], help="Sort the output by the length of the first column. 'asc' for lowest to longest, 'desc' for longest to lowest.")

    args = parser.parse_args()

    try:
        convert_to_dict(args.input, args.output, args.sort)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

