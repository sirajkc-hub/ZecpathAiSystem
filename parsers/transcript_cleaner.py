FILLER_WORDS = [
    "um",
    "uh",
    "like",
    "you know",
    "actually",
    "basically"
]

def remove_fillers(text):
    text = text.lower()
    fillers = [
        "you know",
        "actually",
        "basically"
    ]
    for filler in fillers:
        text = text.replace(filler, "")
    words = text.split()
    cleaned = []
    for word in words:
        if word not in ["um", "uh", "like"]:
            cleaned.append(word)
    return " ".join(cleaned)

def normalize_case(text):
    return text.lower()

def correct_punctuation(text):
    text = text.strip()
    if not text.endswith("."):
        text += "."
    return text

def detect_silence(text):
    return len(text.strip()) == 0

def detect_partial_answer(text):
    keywords = [
        "don't know",
        "not sure",
        "maybe"
    ]
    for item in keywords:
        if item in text.lower():
            return True
    return False

def fix_interrupted_speech(text):
    text = text.replace("--", " ")
    return text

def clean_transcript(text):
    text = remove_fillers(text)
    text = normalize_case(text)
    text = fix_interrupted_speech(text)
    text = correct_punctuation(text)
    return text

sample_text = """
Um I have 2 years of experience in Python and Django actually
"""
print(clean_transcript(sample_text))