def simulate_interview(candidate):
    return {
        "candidate_id": candidate["candidate_id"],
        "candidate_type": candidate["type"],
        "ai_score": candidate["manual_score"] - 2
    }

def compare_scores(ai_score, manual_score):
    difference = abs(ai_score - manual_score)
    return {
        "ai_score": ai_score,
        "manual_score": manual_score,
        "difference": difference
    }

def detect_inconsistency(difference):
    if difference > 10:
        return True
    return False

def accuracy(ai_score, manual_score):
    difference = abs(ai_score - manual_score)
    return round(
        (1 - difference / 100) * 100,2)

def recommendation(accuracy_score):
    if accuracy_score >= 90:
        return "Model performance is satisfactory."
    return "Improve scoring rules and evaluation logic."

def build_test_report(candidate):
    interview = simulate_interview(candidate)
    comparison = compare_scores(
        interview["ai_score"],
        candidate["manual_score"]
    )
    accuracy_score = accuracy(
        interview["ai_score"],
        candidate["manual_score"]
    )
    return {
        "candidate_id":
            candidate["candidate_id"],
        "candidate_type":
            candidate["type"],
        "comparison":
            comparison,
        "accuracy":
            accuracy_score,
        "recommendation":
            recommendation(accuracy_score)
    }

if __name__ == "__main__":
    candidate = {
        "candidate_id": "C001",
        "type": "Confident",
        "manual_score": 92
    }
    report = build_test_report(candidate)
    print(report)
