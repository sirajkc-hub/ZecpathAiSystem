def detect_poor_audio(confidence_score):
    return confidence_score < 0.60

def detect_missing_answer(text):
    return len(text.strip()) == 0

def detect_language_mix(text):
    malayalam_words = [
        "entha",
        "aano",
        "alle"
    ]
    for word in malayalam_words:
        if word in text.lower():
            return True
    return False

def detect_background_noise(noise_level):
    return noise_level > 0.70

def retry_message():
    return (
        "I could not understand your answer. "
        "Could you please repeat it?"
    )

def clarification_message():
    return ("Could you explain that in another way?")

def safety_fallback():
    return ("Let's continue with the next question.")

def build_edge_case_report(
        confidence_score,
        text,
        noise_level):

    return {
        "poor_audio":detect_poor_audio(confidence_score),
        "language_mixing":detect_language_mix(text),
        "missing_answer":detect_missing_answer(text),
        "background_noise":detect_background_noise(noise_level)
    }

if __name__ == "__main__":
    report = build_edge_case_report(
        confidence_score=0.45,
        text="I have 2 years experience alle",
        noise_level=0.80
    )
    print(report)