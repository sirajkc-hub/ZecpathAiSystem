def normalize_resume(resume_data):
    normalized = {
        "skills":resume_data.get("skills",[]),
        "experience":resume_data.get("experience",[]),
        "education":resume_data.get("education",[])}
    return normalized

KEYWORD_WEIGHT = 0.40
SEMANTIC_WEIGHT = 0.60

def normalize_score(score):
    if score > 100:
        return 100
    if score < 0:
        return 0
    return round(score, 2)

def mask_personal_info(text):
    replacements = {"sirajudheen":"[NAME]",
                    "9567300820":"[PHONE]",
                    "sirajkc820@gmail.com":"[EMAIL]"
                    }
    for key, value in replacements.items():
        text = text.replace(key,value)
    return text

BIAS_INDICATORS = ["gender","age","religion","marital status"]

def evaluate_bias(text):
    found = []
    text = text.lower()
    for indicator in BIAS_INDICATORS:
        if indicator in text:
            found.append(
                indicator
            )
    return found

def fair_score(original_score):
    return normalize_score(original_score)

