def fluency_score(text):
    words = len(text.split())
    if words > 30:
        return 1.0
    if words > 15:
        return 0.8
    return 0.5

def grammar_score(text):
    if text.endswith("."):
        return 1.0
    return 0.7

def vocabulary_score(text):
    unique_words = len(set(text.lower().split()))
    total_words = len(text.split())
    if total_words == 0:
        return 0
    return unique_words / total_words

def clarity_score(text):
    words = len(text.split())
    if words > 20:
        return 1.0
    if words > 10:
        return 0.8
    return 0.5
FILLER_WORDS = [
    "um",
    "uh",
    "you know",
    "actually",
    "like"
]
def count_fillers(text):
    count = 0
    text = text.lower()
    for word in FILLER_WORDS:
        count += text.count(word)
    return count

def structure_score(text):
    if "." in text:
        return 1.0
    return 0.6

def communication_score(
        fluency,
        grammar,
        vocabulary,
        clarity,
        structure):
    score = (
        fluency * 0.25 +
        grammar * 0.20 +
        vocabulary * 0.20 +
        clarity * 0.20 +
        structure * 0.15
    )
    return round(score * 100, 2)

def normalize_score(score):
    if score > 95:
        return 95
    if score < 20:
        return 20
    return score

def build_communication_report(text):
    fluency = fluency_score(text)
    grammar = grammar_score(text)
    vocabulary = vocabulary_score(text)
    clarity = clarity_score(text)
    structure = structure_score(text)
    fillers = count_fillers(text)
    score = communication_score(
        fluency,
        grammar,
        vocabulary,
        clarity,
        structure
    )
    score = normalize_score(score)
    return {
        "fluency": fluency,
        "grammar": grammar,
        "vocabulary": vocabulary,
        "clarity": clarity,
        "structure": structure,
        "filler_words": fillers,
        "communication_score": score
    }

if __name__ == "__main__":

    answer = """I have worked on Django projects and developed REST APIs using Python."""
    result = build_communication_report(answer)
    print(result)



