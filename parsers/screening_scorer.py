from parsers.answer_understanding import detect_off_topic
from parsers.answer_understanding import detect_vague_answer

SCORING_PARAMETERS = {
    "clarity": 0.25,
    "relevance": 0.30,
    "completeness": 0.25,
    "consistency": 0.20
}

def score_clarity(answer):
    if len(answer.split()) > 10:
        return 1.0
    if len(answer.split()) > 5:
        return 0.7
    return 0.4

def score_relevance(off_topic):
    if off_topic:
        return 0.0
    return 1.0

def score_completeness(vague):
    if vague:
        return 0.5
    return 1.0

def score_consistency():
    return 1.0

def calculate_question_score(
        clarity,
        relevance,
        completeness,
        consistency):
    score = (
        clarity * SCORING_PARAMETERS["clarity"] +
        relevance * SCORING_PARAMETERS["relevance"] +
        completeness * SCORING_PARAMETERS["completeness"] +
        consistency * SCORING_PARAMETERS["consistency"]
    )
    return round(score * 100, 2)

def normalize_score(score):
    return min(score, 100)

def build_question_score(answer):
    off_topic = detect_off_topic(answer)
    vague = detect_vague_answer(answer)
    clarity = score_clarity(answer)
    relevance = score_relevance(off_topic)
    completeness = score_completeness(vague)
    consistency = score_consistency()
    final_score = calculate_question_score(
        clarity,
        relevance,
        completeness,
        consistency
    )
    return {
        "clarity": clarity,
        "relevance": relevance,
        "completeness": completeness,
        "consistency": consistency,
        "question_score": final_score
    }

def aggregate_screening_score(scores):
    return round(sum(scores) / len(scores),2)

def explain_score(result):
    return {
        "clarity_score":
        result["clarity"],
        "relevance_score":
        result["relevance"],
        "completeness_score":
        result["completeness"],
        "consistency_score":
        result["consistency"],
        "final_score":
        result["question_score"]
    }

sample_answer = """
I have 2 years of Python and Django experience.
"""
result = build_question_score(sample_answer)
print(result)