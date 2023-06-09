import os
import argparse
from resume import Resume
from utils import (
    get_file_list,
    export_to_json
)


def parse_args():
    parser = argparse.ArgumentParser(description="GPT-Resumonator: Automated Resume Information Extraction")
    parser.add_argument("--input-folder", default="./data/input", help="Path to the folder containing resumes")
    parser.add_argument("--output-folder", default="./data/output", help="Path to the folder to save the extracted data")
    parser.add_argument("--summary-length", default=200, type=int, help="Maximum length of generated summaries")
    return parser.parse_args()


def main():
    args = parse_args()

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    file_list = get_file_list(args.input_folder)

    extracted_data = []

    for file_path in file_list:
        resume = Resume(file_path)
        resume.process(args.summary_length)
        extracted_data.append(resume.to_dict())

    export_to_json(extracted_data, args.output_folder)


if __name__ == "__main__":
    main()
