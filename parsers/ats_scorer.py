DEFAULT_WEIGHTS = {
    "skill_match": 0.35,
    "experience": 0.25,
    "education": 0.15,
    "semantic_similarity": 0.25
}

ROLE_WEIGHTS = {
    "data scientist": {
        "skill_match": 0.40,
        "experience": 0.25,
        "education": 0.15,
        "semantic_similarity": 0.20
    },
    "python developer": {
        "skill_match": 0.45,
        "experience": 0.30,
        "education": 0.10,
        "semantic_similarity": 0.15
    }}

def calculate_score(
        skill_score,
        experience_score,
        education_score,
        semantic_score,
        weights):
    final_score = (
        skill_score *
        weights["skill_match"]+experience_score * weights["experience"]+education_score *weights["education"]+
        semantic_score * weights["semantic_similarity"])
    return round(final_score * 100, 2)

def safe_score(value):
    if value is None:
        return 0
    return value

def explain_score(skill_score,experience_score,education_score,semantic_score):
    return {
        "skill_match":skill_score,
        "experience":experience_score,
        "education":education_score,
        "semantic_similarity":semantic_score
    }

def generate_candidate_score():
    weights = ROLE_WEIGHTS["data scientist"]
    skill_score = 0.90
    experience_score = 0.85
    education_score = 0.90
    semantic_score = 0.88
    final_score = calculate_score(
        skill_score,
        experience_score,
        education_score,
        semantic_score,
        weights
    )
    return final_score