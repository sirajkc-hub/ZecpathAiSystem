# Resume Extraction Workflow

from parsers.pdf_reader import extract_pdf_text
from utils.text_cleaner import clean_text

file_path = "data/SIRAJ RESUME (1).pdf"

raw_text = extract_pdf_text(file_path)

cleaned_text = clean_text(raw_text)

print(cleaned_text)

with open("outputs/cleaned_resume.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)


# Job Description Parsing Workflow

from parsers.jd_parser import *

jd_text = read_jd("data/sample_jd.txt")

cleaned_jd = clean_text(jd_text)

jd_object = build_jd_object(cleaned_jd)

print(jd_object)

import json

with open("outputs/jd_output.json", "w") as file:

    json.dump(jd_object, file, indent=4)