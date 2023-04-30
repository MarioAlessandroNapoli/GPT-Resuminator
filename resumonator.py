import os
import argparse
from gpt_resumonator.models.resume import Resume
from gpt_resumonator.utils import (
    get_file_list,
    file_to_text,
    export_data_to_file,
    SUPPORTED_FORMATS
)


def parse_args():
    parser = argparse.ArgumentParser(description="GPT-Resumonator: Automated Resume Information Extraction")
    parser.add_argument("--input-folder", required=True, help="Path to the folder containing resumes")
    parser.add_argument("--output-folder", default="./output", help="Path to the folder to save the extracted data")
    parser.add_argument("--format", default="csv", choices=["csv", "json"],
                        help="Output format for extracted data (csv or json)")
    parser.add_argument("--summary-length", default=200, type=int, help="Maximum length of generated summaries")
    return parser.parse_args()


def main():
    args = parse_args()

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    file_list = get_file_list(args.input_folder, SUPPORTED_FORMATS)

    extracted_data = []

    for file_path in file_list:
        file_extension = os.path.splitext(file_path)[1].lower()
        raw_text = file_to_text(file_path, file_extension)
        resume = Resume(raw_text)
        resume.process(args.summary_length)
        extracted_data.append(resume.to_dict())

    export_data_to_file(extracted_data, args.format, args.output_folder)


if __name__ == "__main__":
    main()