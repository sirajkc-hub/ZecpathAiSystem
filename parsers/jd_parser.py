def read_jd(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

skills_database = [
    "python",
    "sql",
    "django",
    "machine learning",
    "power bi",
    "java"
]

def extract_skills(text):

    found_skills = []

    for skill in skills_database:

        if skill in text:
            found_skills.append(skill)

    return found_skills

roles_database = [
    "python developer",
    "data analyst",
    "machine learning engineer",
    "backend developer"
]

def extract_role(text):

    for role in roles_database:

        if role in text:
            return role

    return "role not found"

import re

def extract_experience(text):

    match = re.search(r'(\d+)\s+years', text)

    if match:
        return match.group(1) + " years"

    return "not specified"

education_keywords = [
    "b.tech",
    "bsc",
    "mca",
    "mba"
]

def extract_education(text):

    found = []

    for edu in education_keywords:

        if edu in text:
            found.append(edu)

    return found

skill_synonyms = {
    "ml": "machine learning",
    "py": "python",
    "postgres": "postgresql"
}

def build_jd_object(text):

    return {
        "role": extract_role(text),
        "skills": extract_skills(text),
        "experience": extract_experience(text),
        "education": extract_education(text)
    }