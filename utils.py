import os
import json
import openai
from docx2pdf import convert
from typing import List, Dict
from pdfminer.high_level import extract_text

supported_formats = ('.pdf', '.docx', '.txt')
openai.api_key = '##'


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
        new_file_path = os.path.splitext(file_path)[0] + '.pdf'
        text = extract_text(new_file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")
    return text


def get_gpt_response(messages, temp=0.4):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temp,
        stream=True
    )
    res_len = 0
    total_message = ""
    for chunk in res:
        chunk_message = chunk['choices'][0]['delta']  # extract the message
        if 'content' in chunk_message.keys():
            message = chunk_message['content']
            print(f"{message}", end="")
            res_len += len(message)
            total_message += message
    return total_message


def generate_json_response(cv) -> dict:
    cv_message = get_cv_extracion_messages(cv)
    print('------------\nCV\n------------\n')
    json_output = get_gpt_response(cv_message)
    try:
        parsed_json = json.loads(json_output)
        return parsed_json
    except json.JSONDecodeError as error:
        correction_messages = get_json_correction_messages(error, json_output)
        corrected_json_output = get_gpt_response(correction_messages)
        try:
            print('------------\nCORRECTING\n------------\n')
            parsed_json = json.loads(corrected_json_output)
            return parsed_json
        except json.JSONDecodeError as e:
            print(f"Cannot produce output. Error: {e}")


def get_cv_extracion_messages(txt):
    messages = [
        {"role": "system",
         "content": "You are a CV info extractor backend API, you can output only JSON results without any words or explanation, just like an API"},
        {"role": "user", "content": f"I will give you a cv in any possible language and a skeleton for a JSON output you have to fill.\
         \n\n1)Summarize all the job and education description you write to a maximum of 200 chars.\n2)Follow the skeleton schema and output as many information you can find.\
         \n\nCV:{txt}\n\nSKELETON:{skeleton}\n\nJSON RESULT:\n"}
    ]
    return messages


def get_json_correction_messages(error, corrupted_json):
    messages = [
        {"role": "system",
         "content": "You are a JSON CORRECTION API, you can output only JSON results without any words or explanation, just like an API"},
        {"role": "user",
         "content": f"When I try to load this JSON with Python json.loads(json_txt) I receive this error message: {error.msg}.\nCorrect the following JSON to a valid JSON that can be loaded.\n\nJSON:{corrupted_json}"}
    ]
    return messages


def get_summary_messages(cv, summary_length=500):
    messages = [
        {"role": "system", "content": "You are a CV summarization tool"},
        {"role": "user", "content": f"I will give you a cv in any possible language, you have to summarize it in {summary_length} chars.\
         \n\nCV:{cv}"}
    ]
    return messages


def get_gpt_summary(cv, summary_length):
    summary_prompt = get_summary_messages(cv, summary_length)
    print('------------\nSUMMARY\n------------\n')
    summary_txt = get_gpt_response(summary_prompt, 1)
    return summary_txt


skeleton = """
{
    contact_info:{
        name:str,
        location:str,
        address:str,
        phone:str,
        email:str,
    }
    work_experience:[
        {
            title:str,
            company:str,
            location:str,
            start:date,
            end:date,
            description(summary in 200 chars):str
        },
        ...,
        ...
    ],
    education:[
        {
            degree:str,
            institution:str,
            location:str,
            start:str,
            end:str,
            description(summary in 200 chars):str
            grade:str,
            thesis_title:str
        },
        ...,
        ...
    ]
    skills:{
        category:[skills],
        category:[skills],
        ...
    }
    companies_worked_for:[
        {
            name:str,
            location:str
        },
        ...,
        ...
    ]
}
"""
