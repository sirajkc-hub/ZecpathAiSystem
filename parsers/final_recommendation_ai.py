DECISION_RULES = {
    "selected": 85,
    "review": 65
}

def recommend_candidate(hiring_fit_score):
    if hiring_fit_score >= DECISION_RULES["selected"]:
        return "Selected"
    if hiring_fit_score >= DECISION_RULES["review"]:
        return "Hold / Review"
    return "Rejected"

def decision_confidence(
        hiring_fit_score):
    if hiring_fit_score >= 85:
        return 0.95
    if hiring_fit_score >= 65:
        return 0.80
    return 0.60

def evaluate_risk(
        behavioral_score,
        integrity_score):
    risk = []
    if behavioral_score < 60:
        risk.append("Behavioral Risk")
    if integrity_score < 70:
        risk.append("Integrity Risk")
    return risk

def explain_decision():
    return {
        "Hiring Fit":"Cross-round aggregated score",
        "Behavior":"Behavioral analysis",
        "Integrity":"Interview integrity",
        "Confidence":"Decision confidence level"
    }

def build_decision_output(
        candidate_id,
        hiring_fit_score,
        behavioral_score,
        integrity_score):
    decision = recommend_candidate(hiring_fit_score)
    confidence = decision_confidence(hiring_fit_score)
    risks = evaluate_risk(behavioral_score,integrity_score)
    return {
        "candidate_id": candidate_id,
        "hiring_fit_score": hiring_fit_score,
        "recommendation": decision,
        "confidence_score": confidence,
        "risk_factors": risks,
        "explanation": explain_decision()
    }

if __name__ == "__main__":

    report = build_decision_output(
        "C001",
        89,
        82,
        90
    )
    print(report)