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

def detect_repeated_words(text):
    words = text.lower().split()
    repeated = []
    for word in set(words):
        if words.count(word) > 2:
            repeated.append(word)
    return repeated

def stress_score(
        hesitation_count,
        uncertainty,
        repeated_words):
    score = 0
    score += hesitation_count * 10
    if uncertainty:
        score += 20
    score += len(repeated_words) * 10
    return min(score, 100)

def behavioral_confidence_score(
        communication_strength,
        stress):
    score = communication_strength * 100
    score -= stress * 0.5
    return max(score, 0)



def build_confidence_object(text):
    hesitation = detect_hesitation(text)
    uncertainty = detect_uncertainty(text)
    repeated_words = detect_repeated_words(text)
    stress = stress_score(
        hesitation,
        uncertainty,
        repeated_words
    )
    behavior_score = behavioral_confidence_score(
        communication_strength(
            hesitation,
            uncertainty
        ),
        stress
    )
    return {
        "hesitation_count":hesitation,
        "response_length":response_length(text),
        "response_pace":response_pace(text),
        "sentiment_score":sentiment_score(text),
        "uncertainty":uncertainty,
        "contradiction":detect_contradiction(text),
        "communication_strength":communication_strength(hesitation,uncertainty),
        "repeated_words": repeated_words,
        "stress_score":stress,
        "behavioral_confidence_score":behavior_score,
    }

if __name__ == "__main__":
    text = """I think I worked with Python.
    Maybe I can solve this problem."""
    report = build_confidence_object(text)
    print(report)

