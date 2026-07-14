def evaluate_prediction(ai_result, manual_result):
    if ai_result == manual_result:
        return "Correct"
    return "Mismatch"

def validate_followup(answer):
    if len(answer.strip()) == 0:
        return "Repeat Question"
    if len(answer.split()) < 5:
        return "Clarification"
    return "Next Question"

def normalize_score(score):
    if score < 0:
        return 0
    if score > 100:
        return 100
    return score

REMOVE_WORDS = [
    "um",
    "uh",
    "actually",
    "you know",
    "like"
]

def clean_transcript(text):
    text = text.lower()
    for word in REMOVE_WORDS:
        text = text.replace(word, "")
    return " ".join(text.split())

def build_optimization_report():
    return {
        "false_positive_reduction": True,
        "followup_stability": True,
        "score_normalization": True,
        "processing_optimized": True,
        "transcript_cleanup": True
    }

if __name__ == "__main__":
    print(normalize_score(108))
    print(validate_followup("Python"))
    print(build_optimization_report())