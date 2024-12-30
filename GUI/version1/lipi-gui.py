#!/usr/bin/env python3

"""
GUI simulation of Lipidiipikar encoding.
Version 1.0.
Written by Ye Kyaw Thu, Language Understanding Lab., Myanmar.
Last updated: 30 December 2024.

How to run:
1. Run the following command in your terminal:
python lipi-gui.py

2. Copy and paste the generated HTTP link (e.g., http://127.0.0.1:5000) into your web browser.

Note: Ensure that the "index.html" file is located in the templates folder.
"""

import re
import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER


def create_break_pattern():
    """Creates and returns the regular expression pattern for Myanmar syllable breaking."""
    my_consonant = r"က-အ"
    en_char = r"a-zA-Z0-9"
    other_char = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-{-~\s"
    subscript_symbol = r"္"
    a_that = r"်"

    return re.compile(
        r"((?<!" + subscript_symbol + r")[" + my_consonant + r"]"
        r"(?![" + a_that + subscript_symbol + r"])"
        + r"|[" + en_char + other_char + r"])"
    )


def process_syllable_with_athat(syllable):
    """
    Splits a syllable containing "်" into two parts, combines "အ" if necessary,
    and concatenates them back into a single syllable.
    """
    if "်" in syllable:
        match = re.match(r"(.*?)([က-အ]်)(.*)", syllable)
        if match:
            first_part, middle_part, second_part = match.groups()
            middle_part_consonant = middle_part[:-1]  # Remove "်" from middle part

            # Add "အ" to single consonants without vowels or medials
            if len(first_part) == 1 and re.match(r"^[က-အ]$", first_part):
                first_part = first_part + "အ"
            # Remove "အ" if it is part of a longer string containing other vowels, medials, or characters
            elif len(first_part) > 1 and first_part.startswith("အ"):
                first_part = first_part[1:]

            # Concatenate the processed first and second parts into one syllable
            combined_syllable = first_part + middle_part_consonant + second_part

            return [combined_syllable]  # Return as a single item

    return [syllable]  # Return as is if no "်" found


def process_text(line, break_pattern):
    """Processes the text line by line for syllable breaking and conversion."""
    # Step 1: Substitute "္" with "်" and "ါ" with "ာ"
    line = line.replace("္", "်").replace("ါ", "ာ").replace("ဣ", "အိ").replace("ဤ", "အီ").replace("ဥ", "အု").replace("ဦ", "အူ").replace("ဧ", "အေ").replace("ဩ", "အော").replace("ဪ", "အော်").replace("ဿ", "သ").replace("၌", "နှိုက်").replace("၍", "ရွေ့").replace("၎င်း", "လည်းကောင်း").replace("၏", "အိ")

    # Step 2: Delete "၊", "။", and other symbols
    line = re.sub(r"[၊။!-/:-@[-`{-~]", "", line)

    # Step 3: Apply syllable segmentation
    syllables = break_syllables(line, break_pattern).split(" ")

    # Step 4: Substitute Myanmar consonants
    consonant_substitutions = {
        "ဃ": "ဂ", "ဈ": "ဇ", "ဋ": "တ", "ဌ": "ထ",
        "ဍ": "ဒ", "ဎ": "ဒ", "ဏ": "န", "ဓ": "ဒ",
        "ဗ": "ဘ", "ဠ": "လ"
    }
    #syllables = [consonant_substitutions.get(syl, syl) for syl in syllables]
    # Substitute characters in each syllable
    syllables = [
        ''.join(consonant_substitutions.get(char, char) for char in syl) 
        for syl in syllables
    ]

    # Step 5: Add "အ" for consonants without vowels
    syllables = [
        syl + "အ" if re.match(r"^[က-အ]$", syl) and syl != "အ" else syl
        for syl in syllables
    ]

    # Step 6: Process syllables with "Athat"
    syllables_processed = []
    for syl in syllables:
        result = process_syllable_with_athat(syl)
        syllables_processed.extend(result)  # Append processed parts to the list

    # Debug: Print intermediate syllables before vowel substitutions
    #print("Before vowel substitutions:", syllables_processed)

    # Step 7: Apply vowel substitutions
    vowel_substitutions = {
    "ျှိုဝ်း": "ယဟအိုဝး",
    "ျှော့": "ယဟဩ့",
    "ျှော်": "ယဟဪ",
    "ျှိုး": "ယဟအိုး",
    "ြှုံး": "ရဟအုံး",
    "ြှော့": "ရဟဩ့",
    "ြှော်": "ရဟဪ",
    "ျော့": "ယဩ့",
    "ျော်": "ယဪ",
    "ျိုး": "ယအိုး",
    "ြော့": "ရဩ့",
    "ြော်": "ရဪ",
    "ြိုး": "ရအိုး",
    "ှေါ့": "ဟဩ့",
    "ှေါ်": "ဟဪ",
    "ှော့": "ဟဩ့",
    "ှော်": "ဟဪ",
    "ျှား": "ယဟအား",
    "ျှီး": "ယဟဤး",
    "ျှူး": "ယဟဦး",
    "ျှေး": "ယဟဧး",
    "ျှဲ့": "ယဟဧဲ့",
    "ျှော": "ယဟဩ",
    "ျှံ့": "ယဟအံ့",
    "ြှီး": "ရဟဤး",
    "ြှူး": "ရဟဦး",
    "ြှေး": "ရဟဧး",
    "ြှဲ့": "ရဟဧဲ့",
    "ြှံ့": "ရဟအံ့",
    "ြှား": "ရဟအား",
    "ျွီး": "ယဝဤး",
    "ျွေး": "ယဝဧေး",
    "ျွဲ့": "ယဝဧဲ့",
    "ျွံ့": "ယဝအံ့",
    "ျွား": "ယွအား",
    "ြွီး": "ရဝဤး",
    "ြွေး": "ရဝဧး",
    "ြွဲ့": "ရဝဧဲ့",
    "ြွံ့": "ရဝအံ့",
    "ြွား": "ရဝအား",
    "ွှီး": "ဝဟဤး",
    "ွှေး": "ဝဟဧး",
    "ွှဲ့": "ဝဟဧဲ့",
    "ွှံ့": "ဝဟအံ့",
    "ွှား": "ဝဟအား",
    "ော့": "ဩ့",
    "ော်": "ဪ",
    "ိုး": "အိုး",
    "ေါ့": "ဩ့",
    "ေါ်": "ဪ",
    "ျီး": "ယဤး",
    "ျူး": "ယဦး",
    "ျေး": "ယဧး",
    "ျဲ့": "ယဧဲ့",
    "ျော": "ယဩ",
    "ျံ့": "ယအံ့",
    "ျား": "ယအား",
    "ျို": "ယအို",
    "ျုံ": "ယဥံ",
    "ြီး": "ရဤး",
    "ြူး": "ရဦး",
    "ြေး": "ရဧး",
    "ြဲ့": "ရဧဲ့",
    "ြော": "ရဩ",
    "ြံ့": "ရအံ့",
    "ြား": "ရအား",
    "ြို": "ရအို",
    "ှီး": "ဟဤး",
    "ှူး": "ဟဦး",
    "ှေး": "ဟဧး",
    "ှဲ့": "ဟဧဲ့",
    "ှံ့": "ဟအံ့",
    "ှုံ": "ဟဥံ",
    "ှား": "ဟအား",
    "ှော": "ဟဩ",
    "ျှာ": "ယဟအာ",
    "ျှိ": "ယဟဣ",
    "ျှီ": "ယဟဤ",
    "ျှု": "ယဟဥ",
    "ျှူ": "ယဟဦ",
    "ျှေ": "ယဟဧ",
    "ျှဲ": "ယဟဧဲ",
    "ျှံ": "ယဟအံ",
    "ြှာ": "ရဟအာ",
    "ြှိ": "ရဟဣ",
    "ြှီ": "ရဟဤ",
    "ြှု": "ရဟဥ",
    "ြှူ": "ရဟဦ",
    "ြှဲ": "ရဟဧဲ",
    "ြှံ": "ရဟအံ",
    "ွီး": "ဝဤး",
    "ွေး": "ဝဧး",
    "ွဲ့": "ဝဧဲ့",
    "ွံ့": "ဝအံ့",
    "ွား": "ဝအား",
    "ွါး": "ဝအား",
    "ျွာ": "ယဝအာ",
    "ျွိ": "ယဝဣ",
    "ျွေ": "ယဝဧ",
    "ျွဲ": "ယဝဧဲ",
    "ြွာ": "ရဝအာ",
    "ြွိ": "ရဝဣ",
    "ြွီ": "ရဝဤ",
    "ြွေ": "ရဝဧ",
    "ြွဲ": "ရဝဧဲ",
    "ြုံ": "ရဥံ",
    "ွှာ": "ဝဟအာ",
    "ွှိ": "ဝဟဣ",
    "ွှီ": "ဝဟဤ",
    "ွှေ": "ဝဟဧ",
    "ွှဲ": "ဝဟဧဲ",
    "ှို": "ဟအို",
    "ီး": "ဤး",
    "ူး": "ဦး",
    "ေး": "ဧး",
    "ဲ့": "ဧဲ့",
    "ော": "ဩ",
    "ံ့": "အံ့",
    "ား": "အား",
    "ို": "အို",
    "ေါ": "ဩ",
    "ါး": "အား",
    "ျာ": "ယအာ",
    "ျိ": "ယဣ",
    "ျီ": "ယဤ",
    "ျု": "ယဥ",
    "ျူ": "ယဦ",
    "ျေ": "ယဧ",
    "ျံ": "ယအံ",
    "ြာ": "ရအာ",
    "ြိ": "ရဣ",
    "ြီ": "ရဤ",
    "ြု": "ရဥ",
    "ြူ": "ရဦ",
    "ြေ": "ရဧ",
    "ြဲ": "ရဧဲ",
    "ြံ": "ရအံ",
    "ှါ": "ဟအာ",
    "ှိ": "ဟဣ",
    "ှီ": "ဟဤ",
    "ှု": "ဟဥ",
    "ှေ": "ဟဧ",
    "ုံ": "ဥံ",
    "ှာ": "ဟအာ",
    "ှဲ": "ဟဧဲ",
    "ျှ": "ယဟအ",
    "ြှ": "ရဟအ",
    "ွာ": "ဝအာ",
    "ွိ": "ဝဣ",
    "ွီ": "ဝဤ",
    "ွဲ": "ဝဧဲ",
    "ွါ": "ဝအာ",
    "ွေ": "ဝဧ",
    "ွံ": "ဝအံ",
    "ျွ": "ယဝအ",
    "ြွ": "ရဝအ",
    "ွှ": "ဝဟအ",
    "ာ": "အာ",
    "ိ": "ဣ",
    "ီ": "ဤ",
    "ု": "ဥ",
    "ူ": "ဦ",
    "ေ": "ဧ",
    "ံ": "အံ",
    "ါ": "အာ",
    "ျ": "ယအ",
    "ြ": "ရအ",
    "ှ": "ဟအ",
    "ွ": "ဝအ"
}


    # Ensure longest substitutions are applied first
    sorted_keys = sorted(vowel_substitutions.keys(), key=len, reverse=True)
    pattern = re.compile("|".join(re.escape(k) for k in sorted_keys))

    syllables_processed = [
        pattern.sub(lambda m: vowel_substitutions[m.group(0)], syl) for syl in syllables_processed
    ]

    # Debug: Print final processed syllables after vowel substitutions
    #print("After vowel substitutions:", syllables_processed)

    return " ".join(syllables_processed)


def break_syllables(line, break_pattern, separator=" "):
    """Applies syllable breaking rules to a line."""
    line = re.sub(r'\s+', ' ', line.strip())
    segmented_line = break_pattern.sub(separator + r"\1", line)
    if segmented_line.startswith(separator):
        segmented_line = segmented_line[len(separator):]
    return segmented_line


@app.route("/", methods=["GET", "POST"])
def index():
    """Render the main interface for text processing."""
    output_text = ""
    input_text = ""
    if request.method == "POST":
        if "clean" in request.form:
            input_text = ""
            output_text = ""
        else:
            input_text = request.form.get("input_text", "")
            file = request.files.get("input_file")

            if file:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(filepath)
                with open(filepath, "r", encoding="utf-8") as f:
                    input_text = f.read()  # Load file content into input_text

            if input_text.strip():
                break_pattern = create_break_pattern()
                
                # Split input_text into lines, process each line, and preserve line breaks
                input_lines = input_text.splitlines()
                processed_lines = [process_text(line, break_pattern) for line in input_lines]
                output_text = "\n".join(processed_lines)

                # Save the output to a file
                output_filepath = os.path.join(app.config["OUTPUT_FOLDER"], "output.txt")
                with open(output_filepath, "w", encoding="utf-8") as f:
                    f.write(output_text)

    return render_template("index.html", output_text=output_text, input_text=input_text)

@app.route("/download", methods=["GET"])
def download_output():
    """Download the processed output file."""
    output_filepath = os.path.join(app.config["OUTPUT_FOLDER"], "output.txt")
    if os.path.exists(output_filepath):
        return send_file(output_filepath, as_attachment=True, download_name="output.txt")
    return "No file available for download", 404


if __name__ == "__main__":
    app.run(debug=True)
