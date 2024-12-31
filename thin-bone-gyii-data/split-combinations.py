import os
import re
import argparse

def split_combinations(input_file, extension):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.read()

    # Regex to match each combination block
    combination_pattern = r"## Combination-(\d+)(.*?)\n(.*?)(?=\n## Combination-\d+|$)"
    matches = re.findall(combination_pattern, data, re.S)

    # Create output files for each match
    for match in matches:
        combination_number = match[0]
        header = f"## Combination-{combination_number}{match[1]}".strip()
        content = match[2].strip()

        # Prepare the output filename
        output_filename = f"combination-{combination_number.lower()}.{extension}"

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(f"{header}\n\n{content}\n")

        print(f"Written: {output_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split combinations into separate files.")
    parser.add_argument("--input", required=True, help="Input filename containing the combinations.")
    parser.add_argument("--extension", required=True, help="Output file extension (e.g., txt).")

    args = parser.parse_args()

    split_combinations(args.input, args.extension)

