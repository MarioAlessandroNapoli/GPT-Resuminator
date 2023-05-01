import os
import csv
import json
import openai
from docx2pdf import convert
from typing import List, Dict
from pdfminer.high_level import extract_text

supported_formats = ('.pdf', '.docx', '.txt')


def get_file_list(folder_path: str) -> List[str]:
    """
    Retrieves a list of files with supported formats from the specified folder.
    :param folder_path: Path to the folder containing resumes.
    :return: A list of file paths with supported formats.
    """
    file_list = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in supported_formats:
                file_list.append(os.path.join(root, file))
    return file_list


def export_data_to_file(data: List[Dict], file_format: str, output_folder: str) -> None:
    """
    Exports the extracted resume data to a file in the specified format (CSV or JSON).

    :param data: A list of dictionaries containing the extracted resume data.
    :param file_format: The output file format (CSV or JSON).
    :param output_folder: The folder to save the exported file.
    """
    if file_format.lower() == "csv":
        export_to_csv(data, output_folder)
    elif file_format.lower() == "json":
        export_to_json(data, output_folder)
    else:
        raise ValueError(f"Unsupported file format: {file_format}")


def export_to_csv(data: List[Dict], output_folder: str) -> None:
    output_file = os.path.join(output_folder, "resume_data.csv")

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)


def export_to_json(data: List[Dict], output_folder: str) -> None:
    output_file = os.path.join(output_folder, "resume_data.json")

    with open(output_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


def file_to_text(file_path: str, file_extension: str) -> str:
    """
    Extracts all text from a file with the given file_path and file_extension.

    :param file_path: The path to the file.
    :param file_extension: The file's extension (e.g., .pdf or .docx).
    :return: The extracted text as a string.
    """
    if file_extension.lower() == ".pdf":
        text = extract_text(file_path)
    elif file_extension.lower() == ".docx":
        convert(file_path)
        new_file_path = os.path.splitext(file_path)[0]+'.pdf'
        text = extract_text(new_file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")
    return text


def generate_text(messages: List[Dict[str, str]]) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content']
