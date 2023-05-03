# GPT-Resuminator

GPT-Resuminator is an innovative tool that streamlines the process of extracting information from resumes using the ChatGPT API. Save time and resources by allowing GPT-Resuminator to handle the tedious task of resume screening for you. Simply upload your resumes and let the magic happen!

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [API Integration](#api-integration)
6. [Contributing](#contributing)
7. [License](#license)

## Features
- Bulk resume upload and processing
- Support for multiple file formats (PDF, DOCX, TXT)
- Information extraction for key resume data (contact info, education, experience, skills, etc.)
- Summary generation for quick candidate assessment
- Export of extracted data to CSV or JSON formats
- Integration with the ChatGPT API for enhanced resume parsing
- Configurable parameters to tailor the extraction process

## Installation
To install GPT-Resuminator, follow these simple steps:

1. Clone the repository:
```
git clone https://github.com/MarioAlessandroNapoli/GPT-Resuminator
```

2. Change the working directory to GPT-Resuminator:
```
cd GPT-Resuminator
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Set up the environment variables for the ChatGPT API key:
```
export CHATGPT_API_KEY=your_api_key_here
```

## Usage
To run GPT-Resuminator, execute the following command in the terminal:
```
python resumonator.py --input-folder /path/to/resumes
```

You can also specify optional arguments, such as output format or summary length. For a full list of options, run:
```
python resumonator.py --help
```

## Project Structure
The GPT-Resuminator project is organized as follows:

```
GPT-Resuminator/
│
├── gpt_resumonator/
│   ├── __init__.py
│   ├── resumonator.py
│   ├── utils.py
│   └── models/
│       ├── __init__.py
│       ├── resume.py
├── .gitignore
├── README.md
└── LICENSE
```

## API Integration
GPT-Resuminator uses the ChatGPT API to enhance the information extraction process. To set up and use the API, follow these steps:

1. Sign up for an API key from the [OpenAI website](https://beta.openai.com/signup/).
2. Store your API key as an environment variable (see [Installation](#installation) step 4).
3. GPT-Resuminator will automatically use the API key to access the ChatGPT API when processing resumes.

## Contributing
We welcome contributions from the community! If you'd like to get involved, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
```
git checkout -b my-new-feature
```

3. Make changes to the codebase and commit your changes:
```
git add .
git commit -m "Add my new feature"
```

4. Push your changes to your fork:
```
git push origin my-new-feature
```

5. Create a pull request on the original GPT-Resuminator repository.

Please ensure that your code adheres to our coding standards and guidelines. Before submitting a pull request, make sure to update the documentation and add any necessary tests.

## License
GPT-Resuminator is released under the [GNU GPL License](https://github.com/MarioAlessandroNapoli/GPT-Resuminator/blob/main/LICENSE).

## Support
If you encounter any issues or have questions, please create an issue on the [GitHub repository](https://github.com/MarioAlessandroNapoli/GPT-Resuminator/issues).

## Acknowledgements
We would like to express our gratitude to the following projects and resources, which inspired and facilitated the development of GPT-Resuminator:

- [OpenAI](https://openai.com/) for creating the ChatGPT API
- [pdfminer](https://github.com/pdfminer/pdfminer.six) for PDF file handling
- [python-docx](https://github.com/python-openxml/python-docx) for DOCX file handling

Thank you for your interest in GPT-Resuminator! With your support, we can continue to improve and refine this powerful tool for resume processing.
