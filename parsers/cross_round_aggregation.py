ROLE_WEIGHTS = {

    "python developer": {
        "ats": 0.20,
        "screening": 0.15,
        "hr": 0.15,
        "technical": 0.30,
        "machine_test": 0.20
    },

    "data scientist": {
        "ats": 0.20,
        "screening": 0.15,
        "hr": 0.15,
        "technical": 0.25,
        "machine_test": 0.25
    }
}

def aggregate_score(
        ats,
        screening,
        hr,
        technical,
        machine_test,
        role):
    weights = ROLE_WEIGHTS[role]
    score = (
        ats * weights["ats"] +
        screening * weights["screening"] +
        hr * weights["hr"] +
        technical * weights["technical"] +
        machine_test * weights["machine_test"]
    )
    return round(score, 2)

def hiring_fit(score):
    return round(score, 2)

def normalize_score(score):
    if score > 100:
        return 100
    if score < 0:
        return 0
    return score

def explain_score():
    return {
        "ATS":"Resume Evaluation",
        "Screening":"Initial Screening",
        "HR":"HR Interview",
        "Technical":"Technical Interview",
        "Machine Test":"Coding Assessment"
    }

def build_candidate_score(
        candidate_id,
        role,
        ats,
        screening,
        hr,
        technical,
        machine_test):
    final_score = aggregate_score(
        ats,
        screening,
        hr,
        technical,
        machine_test,
        role
    )
    final_score = normalize_score(final_score)
    return {
        "candidate_id": candidate_id,
        "role": role,
        "ats_score": ats,
        "screening_score": screening,
        "hr_score": hr,
        "technical_score": technical,
        "machine_test_score": machine_test,
        "hiring_fit_score": final_score,
        "explanation": explain_score()
    }

if __name__ == "__main__":
    report = build_candidate_score(
        "C001",
        "python developer",
        88,
        90,
        85,
        92,
        87
    )
    print(report)

