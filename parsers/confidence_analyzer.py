HESITATION_WORDS = [
    "um",
    "uh",
    "maybe",
    "not sure",
    "i think"
]
def detect_hesitation(text):
    count = 0
    text = text.lower()
    for word in HESITATION_WORDS:
        count += text.count(word)
    return count

def response_length(text):
    return len(text.split())

def response_pace(text):
    words = len(text.split())
    if words > 30:
        return "Detailed"
    if words > 10:
        return "Balanced"
    return "Short"

POSITIVE_WORDS = [
    "confident",
    "experienced",
    "skilled",
    "success",
    "excellent"
]
NEGATIVE_WORDS = [
    "difficult",
    "problem",
    "weak",
    "failure"
]

def sentiment_score(text):
    text = text.lower()
    positive = 0
    negative = 0
    for word in POSITIVE_WORDS:
        positive += text.count(word)
    for word in NEGATIVE_WORDS:
        negative += text.count(word)
    return positive - negative

def detect_uncertainty(text):
    indicators = [
        "maybe",
        "not sure",
        "possibly",
        "i think"
    ]
    for item in indicators:
        if item in text.lower():
            return True
    return False

def detect_contradiction(text):
    text = text.lower()
    if "yes" in text and "no" in text:
        return True
    return False

def communication_strength(hesitation_count,uncertainty):
    score = 1.0
    score -= hesitation_count * 0.1
    if uncertainty:
        score -= 0.2
    return max(score, 0)

def build_confidence_object(text):
    hesitation = detect_hesitation(text)
    uncertainty = detect_uncertainty(text)
    return {
        "hesitation_count":
        hesitation,
        "response_length":
        response_length(text),
        "response_pace":
        response_pace(text),
        "sentiment_score":
        sentiment_score(text),
        "uncertainty":
        uncertainty,
        "contradiction":
        detect_contradiction(text),
        "communication_strength":
        communication_strength(hesitation,uncertainty)
    }

if __name__ == "__main__":
    sample_answer = """
    I am confident in Python development.
    I have excellent experience with Django.
    """
    print(build_confidence_object(sample_answer))

