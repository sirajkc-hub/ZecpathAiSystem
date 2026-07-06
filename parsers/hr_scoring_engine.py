WEIGHTS = {
    "answer_relevance": 0.35,
    "communication": 0.25,
    "confidence": 0.25,
    "consistency": 0.15
}

def generate_hr_score(answer_relevance,communication,confidence,consistency):
    score = (
        answer_relevance * WEIGHTS["answer_relevance"] +
        communication * WEIGHTS["communication"] +
        confidence * WEIGHTS["confidence"] +
        consistency * WEIGHTS["consistency"]
    )
    return round(score * 100, 2)

def score_breakdown(
        answer_relevance,
        communication,
        confidence,
        consistency):
    return {
        "answer_relevance": answer_relevance,
        "communication": communication,
        "confidence": confidence,
        "consistency": consistency
    }

def normalize_score(
        score,
        question_count):
    if question_count == 0:
        return 0
    factor = min(question_count / 10, 1)
    return round(score * factor, 2)

def build_hr_report(candidate_id,answer_relevance,communication,confidence,consistency,question_count):
    raw_score = generate_hr_score(
        answer_relevance,
        communication,
        confidence,
        consistency
    )
    final_score = normalize_score(raw_score,question_count)

    return {
        "candidate_id": candidate_id,
        "answer_relevance_score": answer_relevance,
        "communication_score": communication,
        "confidence_score": confidence,
        "consistency_score": consistency,
        "final_hr_score": final_score
    }

if __name__ == "__main__":
    report = build_hr_report(
        "C001",
        0.85,
        0.88,
        0.90,
        0.95,
        10
    )
    print(report)