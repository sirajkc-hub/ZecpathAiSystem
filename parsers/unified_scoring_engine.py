ROUND_WEIGHTS = {
    "ats": 0.35,
    "screening": 0.30,
    "hr": 0.35
}

ROLE_WEIGHTS = {
    "python developer": {
        "ats": 0.40,
        "screening": 0.25,
        "hr": 0.35
    },
    "data scientist": {
        "ats": 0.35,
        "screening": 0.35,
        "hr": 0.30
    }
}
def unified_score(
        ats,
        screening,
        hr,
        role):
    weights = ROLE_WEIGHTS.get(
        role,
        ROUND_WEIGHTS
    )
    score = (
        ats * weights["ats"] +
        screening * weights["screening"] +
        hr * weights["hr"]
    )
    return round(score, 2)


def hiring_fit(score):
    return round(score, 2)

def recommendation(score):
    if score >= 85:
        return "Hire"
    if score >= 70:
        return "Further Interview"
    return "Reject"

def build_candidate_object(
        candidate_id,
        role,
        ats,
        screening,
        hr):

    score = unified_score(
        ats,
        screening,
        hr,
        role
    )
    return {
        "candidate_id":candidate_id,
        "role":role,
        "ats_score":ats,
        "screening_score":screening,
        "hr_score":hr,
        "hiring_fit_percentage":hiring_fit(score),
        "recommendation":recommendation(score)
    }
if __name__ == "__main__":
    report = build_candidate_object(
        "C001",
        "python developer",
        90,
        88,
        92
    )
    print(report)

