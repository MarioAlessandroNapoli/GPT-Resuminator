import os
from utils import file_to_text, supported_formats, generate_json_response, get_gpt_summary


class Resume:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_extension = os.path.splitext(file_path)[1].lower()
        self.contact_info, self.experience, self.education, self.skills, self.companies_worked_for, self.summary = [None]*6

        if self.file_extension not in supported_formats:
            raise ValueError(f"Unsupported file format: {self.file_extension}")

        self.raw_text = file_to_text(self.file_path, self.file_extension)

    def process(self, summary_length: int):
        cv_output = generate_json_response(self.raw_text)
        self.contact_info = cv_output.get('contact_info')
        self.experience = cv_output.get('contact_info')
        self.education = cv_output.get('contact_info')
        self.skills = cv_output.get('contact_info')
        self.companies_worked_for = cv_output.get('contact_info')
        self.summary = get_gpt_summary(self.raw_text, summary_length)

    def to_dict(self):
        return {
            "file_path": self.file_path,
            "contact_info": self.contact_info,
            "experience": self.experience,
            "education": self.education,
            "skills": self.skills,
            "companies_worked_for": self.companies_worked_for,
            "summary": self.summary,
        }
