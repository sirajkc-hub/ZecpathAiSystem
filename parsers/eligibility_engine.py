ROLE_RULES = {
    "python developer": {
        "min_score": 70,
        "mandatory_skills": [
            "python",
            "sql",
            "django"
        ],
        "min_experience": 2
    },

    "data scientist": {
        "min_score": 75,
        "mandatory_skills": [
            "python",
            "pandas",
            "machine learning"
        ],
        "min_experience": 1
    }
}

def check_score(score, min_score):
    return score >= min_score

def check_skills(candidate_skills, mandatory_skills):
    for skill in mandatory_skills:
        if skill not in candidate_skills:
            return False
    return True

def check_experience(candidate_exp,required_exp):
    return candidate_exp >= required_exp

def evaluate_candidate(score,skills,experience,role):
    rules = ROLE_RULES[role]
    score_ok = check_score(score,rules["min_score"])
    skills_ok = check_skills(skills,rules["mandatory_skills"])
    exp_ok = check_experience(experience,rules["min_experience"])
    if score_ok and skills_ok and exp_ok:
        return "Eligible"
    if score_ok:
        return "Review"
    return "Rejected"

