DEGREES = [
    "bsc",
    "b.tech",
    "bachelor of technology",
    "mca",
    "mba",
    "msc",
    "phd"
]

def extract_degree(text):

    found = []
    text = text.lower()
    for degree in DEGREES:
        if degree in text:
            found.append(degree)
    return found

FIELDS = [
    "computer science",
    "information technology",
    "data science",
    "artificial intelligence",
    "electronics"
]

def extract_field(text):

    found = []
    text = text.lower()
    for field in FIELDS:
        if field in text:
            found.append(field)
    return found

INSTITUTIONS = [
    "calicut university",
    "iit",
    "nit",
    "anna university"
]

def extract_institution(text):

    found = []
    text = text.lower()
    for institution in INSTITUTIONS:
        if institution in text:
            found.append(institution)
    return found

import re
def extract_graduation_year(text):
    years = re.findall(r'20\d{2}', text)
    return years

CERTIFICATIONS = [
    "digital forensics internship",
    "data science",
    "aws",
    "google analytics",
    "power bi"
]

def extract_certifications(text):

    found = []
    text = text.lower()
    for cert in CERTIFICATIONS:
        if cert in text:
            found.append(cert)
    return found

NORMALIZATION = {
    "bsc": "Bachelor of Science",
    "mba": "Master of Business Administration",
    "mca": "Master of Computer Applications"
}
def normalize_degree(degree):
    return NORMALIZATION.get(degree, degree)

CERTIFICATION_CATEGORY = {
    "digital forensics internship":
        "cybersecurity",
    "data science":
        "artificial intelligence",
    "aws":
        "cloud computing"
}

def education_relevance(field, target_role):
    if target_role == "data scientist":
        if field == "computer science":
            return 0.9
        if field == "data science":
            return 1.0
    return 0.5

def build_academic_profile(text):
    return {
        "degree":extract_degree(text),
        "field":extract_field(text),
        "institution":extract_institution(text),
        "graduation_year":extract_graduation_year(text),
        "certifications":extract_certifications(text)
    }