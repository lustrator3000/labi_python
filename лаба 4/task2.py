import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # TODO read file
        with open(OUTPUT_FILENAME, 'w') as f:
            json.dump(data, f, indent=4)
    # TODO otstupi

if __name__ == '__main__':
    # proverka
    task()
    with open(OUTPUT_FILENAME) as f:
        for line in f:
            print(line, end="")
