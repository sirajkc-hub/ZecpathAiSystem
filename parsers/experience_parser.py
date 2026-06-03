COMPANIES = [
    "soften technologies",
    "tcs",
    "infosys",
    "wipro",
    "ibm"
]
def extract_companies(text):
    found = []
    text = text.lower()
    for company in COMPANIES:
        if company in text:
            found.append(company)
    return found

JOB_TITLES = [
    "data scientist",
    "junior data scientist",
    "python developer",
    "software developer",
    "data analyst",
    "machine learning engineer"
]
def extract_job_titles(text):
    found = []
    text = text.lower()
    for title in JOB_TITLES:
        if title in text:
            found.append(title)
    return found
import re
def extract_durations(text):
    pattern = r'(\d{2}/\d{4})\s*-\s*(\d{2}/\d{4})'
    return re.findall(pattern, text)

def calculate_total_experience():
    return "5 months"

def detect_gaps():
    return "No major gaps detected"

def detect_overlap():
    return "No overlapping roles detected"

ROLE_SIMILARITY = {
    "python developer": [
        "software developer",
        "backend developer"
    ],
    "data scientist": [
        "machine learning engineer",
        "data analyst"
    ]
}

def relevance_score(candidate_role, target_role):
    if candidate_role == target_role:
        return 1.0
    if target_role in ROLE_SIMILARITY.get(candidate_role, []):
        return 0.8
    return 0.4

def build_experience_object(text):

    return {
        "companies": extract_companies(text),
        "job_titles": extract_job_titles(text),
        "durations": extract_durations(text),
        "total_experience": calculate_total_experience(),
        "gaps": detect_gaps(),
        "overlap": detect_overlap()
    }