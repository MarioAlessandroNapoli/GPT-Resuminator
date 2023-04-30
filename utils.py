import os
from typing import List

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
