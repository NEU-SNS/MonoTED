import jiwer
import sys
import os
import re
from num2words import num2words

replacements = {}
for i in range(99):
    replacements[num2words(i)] = str(i)
    if i == 1 or (i % 10 == 1 and i > 20):
        replacements[num2words(i, to='ordinal')] = str(i) + "st"
    if i == 2 or (i % 10 == 2 and i > 20):
        replacements[num2words(i, to='ordinal')] = str(i) + "nd"
    if i == 3 or (i % 10 == 3 and i > 20):
        replacements[num2words(i, to='ordinal')] = str(i) + "rd"
    else:
        replacements[num2words(i, to='ordinal')] = str(i) + "th"

def do_text_to_numbers(text):
    new_text = text
    for i, j in replacements.items():
        new_text = re.sub(r'\b' + i + r'\b', j, new_text)
    return new_text

def do_text_to_symbols(text):
    new_text = text
    new_text = re.sub(r"\b([0-9]+) percent\b", "\\1%", new_text)
    new_text = re.sub(r"\b([0-9]+) dollars{0,1}\b", "$\\1", new_text)
    new_text = re.sub(r"\b([0-9]+) euros{0,1}\b", "€\\1", new_text)
    return new_text


def do_sanitize(text):
    new_text = text.lower().replace('-', '')
    new_text = do_text_to_numbers(new_text)
    new_text = do_text_to_symbols(new_text)
    return new_text

transformation = jiwer.Compose([
    jiwer.RemoveKaldiNonWords(),
    jiwer.RemovePunctuation(),
    jiwer.ToLowerCase(),
    jiwer.SubstituteRegexes({r" '": r"'"}),
    jiwer.RemoveWhiteSpace(replace_by_space=True),
    jiwer.RemoveMultipleSpaces(),
    jiwer.Strip(),
    jiwer.ReduceToListOfListOfWords()
])

def calc_wer(ground_truth_filename, hypothesis_filename):
    with open(ground_truth_filename) as ground_truth_file:
        ground_truth = ground_truth_file.read()

        with open(hypothesis_filename) as hypothesis_file:
            hypothesis = hypothesis_file.read()

    ground_truth = do_sanitize(ground_truth.replace('\n', ' ').replace('\r', '').replace(" '", "'").replace("(", "[").replace(")", "]"))
    hypothesis = do_sanitize(hypothesis.replace('\n', ' ').replace('\r', '').replace(" '", "'").replace("(", "[").replace(")", "]"))
    measures = jiwer.compute_measures(ground_truth, hypothesis, truth_transform=transformation, hypothesis_transform=transformation)
    return measures['wer']

def main():
    # Check that two arguments are passed (excluding the script name itself)
    if len(sys.argv) != 3:
        print("Usage: python calc_wer.py <ground-truth file> <hypothesis file>", file=sys.stderr)
        return 1

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if not os.path.exists(file1):
        print(f"Error: The ground-truth file '{file1}' does not exist.", file=sys.stderr)
        return 1  # Return an e
    if not os.path.exists(file2):
        print(f"Error: The hypothesis '{file2}' does not exist.", file=sys.stderr)
        return 1

    print(str(calc_wer(file1, file2)))    

if __name__ == "__main__":
    sys.exit(main())
