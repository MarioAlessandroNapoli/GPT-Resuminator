import os
from typing import Optional
from utils import file_to_text, detect_language, supported_formats

class Resume:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_extension = os.path.splitext(file_path)[1].lower()
        self.language = None
        self.raw_text = None
        self.contact_info = {}
        self.education = []
        self.experience = []
        self.skills = []
        self.summary = None

        if self.file_extension not in supported_formats:
            raise ValueError(f"Unsupported file format: {self.file_extension}")

        self._extract_text()
        self._detect_language()

    def _extract_text(self):
        self.raw_text = file_to_text(self.file_path, self.file_extension)

    def _detect_language(self):
        self.language = detect_language(self.raw_text)

    def process(self, summary_length: Optional[int] = None):
        self._extract_contact_info()
        self._extract_education()
        self._extract_experience()
        self._extract_skills()
        self._generate_summary(summary_length)

    def _extract_contact_info(self):
        # Implement contact info extraction logic based on self.language and self.raw_text
        return

    def _extract_education(self):
        # Implement education extraction logic based on self.language and self.raw_text
        return

    def _extract_experience(self):
        # Implement experience extraction logic based on self.language and self.raw_text
        return

    def _extract_skills(self):
        # Implement skills extraction logic based on self.language and self.raw_text
        return

    def _generate_summary(self, summary_length: Optional[int] = None):
        # Implement summary generation logic using ChatGPT API
        return

    def to_dict(self):
        return {
            "file_path": self.file_path,
            "language": self.language,
            "contact_info": self.contact_info,
            "education": self.education,
            "experience": self.experience,
            "skills": self.skills,
            "summary": self.summary,
        }
