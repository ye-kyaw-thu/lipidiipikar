#!/bin/bash

## Testing by Ye, LST Lab., Myanmar.
## 30 Dec 2024
## How to run:
## time ./chk-all-combi.sh --folder ./thin-bone-gyii-data/ --extension txt  

# Check for required arguments
if [[ $# -lt 2 ]]; then
    echo "Usage: $0 --folder <folder_path> --extension <file_extension>"
    exit 1
fi

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --folder)
            FOLDER="$2"
            shift 2
            ;;
        --extension)
            EXTENSION="$2"
            shift 2
            ;;
        *)
            echo "Unknown argument: $1"
            exit 1
            ;;
    esac
done

# Ensure the folder exists
if [[ ! -d "$FOLDER" ]]; then
    echo "Error: Folder '$FOLDER' does not exist."
    exit 1
fi

# Process each file in the folder with the specified extension
for INPUT_FILE in "$FOLDER"/*."$EXTENSION"; do
    if [[ -f "$INPUT_FILE" ]]; then
        OUTPUT_FILE="${INPUT_FILE%.$EXTENSION}.lipi"
        echo "Processing: $INPUT_FILE -> $OUTPUT_FILE"
        python ./lipi.py --input "$INPUT_FILE" --output "$OUTPUT_FILE"
    fi
done

echo "All files processed successfully."

