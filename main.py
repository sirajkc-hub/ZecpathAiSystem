# Resume Extraction Workflow

from parsers.pdf_reader import extract_pdf_text
from utils.text_cleaner import clean_text
from parsers.section_classifier import detect_sections

file_path = "data/SIRAJ RESUME (1).pdf"
raw_text = extract_pdf_text(file_path)
cleaned_text = clean_text(raw_text)
print(cleaned_text)

with open("outputs/cleaned_resume.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)
from parsers.jd_parser import *
jd_text = read_jd("data/sample_jd.txt")
cleaned_jd = clean_text(jd_text)
jd_object = build_jd_object(cleaned_jd)
print(jd_object)

import json
with open("outputs/jd_output.json", "w") as file:
    json.dump(jd_object, file, indent=4)

sections = detect_sections(raw_text)
print(sections)

import json
with open("outputs/resume_sections.json", "w") as file:
    json.dump(sections, file, indent=4)

from parsers.skill_extractor import *
skills = extract_skills(raw_text)
skills.extend(
    detect_skill_stack(raw_text)
)
skills = remove_duplicates(skills)
skill_output = build_skill_output(skills)
print(skill_output)

import json
with open(
    "outputs/skills_output.json",
    "w"
) as file:
    json.dump(
        skill_output,
        file,
        indent=4
    )

