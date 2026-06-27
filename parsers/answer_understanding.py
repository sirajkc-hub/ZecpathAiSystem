INTENTS = [
    "skill",
    "experience",
    "availability",
    "salary",
    "education",
    "project",
    "leadership",
    "unknown"
]

def classify_intent(text):
    text = text.lower()
    if "python" in text or "django" in text:
        return "skill"
    if "year" in text or "experience" in text:
        return "experience"
    if "join" in text or "available" in text:
        return "availability"
    if "salary" in text or "lpa" in text:
        return "salary"
    if "project" in text:
        return "project"
    if "team" in text:
        return "leadership"

    if "degree" in text:
        return "education"
    return "unknown"

SKILLS = [
    "python",
    "sql",
    "django",
    "flask",
    "tensorflow",
    "pandas"
]

def extract_skills(text):
    found = []
    for skill in SKILLS:
        if skill in text.lower():
            found.append(skill)
    return found

import re
def extract_experience(text):
    pattern = r'(\d+)\s+year'
    match = re.search(pattern,text.lower())
    if match:
        return int(match.group(1))
    return 0

def extract_availability(text):
    text = text.lower()
    if "immediately" in text:
        return "Immediate"
    if "30 days" in text:
        return "30 Days"
    if "60 days" in text:
        return "60 Days"
    return "Unknown"

import re
def extract_salary(text):
    pattern = r'(\d+)\s*lpa'
    match = re.search(pattern,text.lower())
    if match:
        return match.group(1) + " LPA"
    return "Not Mentioned"

def detect_off_topic(text):
    keywords = [
        "python",
        "experience",
        "salary",
        "join"
    ]
    for item in keywords:
        if item in text.lower():
            return False
    return True

def detect_vague_answer(text):
    vague = [
        "maybe",
        "not sure",
        "don't know"
    ]
    for item in vague:
        if item in text.lower():
            return True
    return False

def build_answer_object(text):
    return {
        "intent":
        classify_intent(text),
        "skills":
        extract_skills(text),
        "experience":
        extract_experience(text),
        "availability":
        extract_availability(text),
        "salary":
        extract_salary(text),
        "off_topic":
        detect_off_topic(text),
        "vague":
        detect_vague_answer(text)
    }

sample_answer = """
I have 2 years of Python and Django experience.
I can join immediately.
Expected salary is 8 LPA.
"""
print(build_answer_object(sample_answer))

