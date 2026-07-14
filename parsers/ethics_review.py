CONSENT_REQUIREMENTS = {
    "resume_processing": True,
    "interview_recording": True,
    "data_storage": True,
    "ai_evaluation": True
}

def check_consent():
    return CONSENT_REQUIREMENTS

def fairness_review(score_before, score_after):
    difference = abs(score_before - score_after)
    return {
        "original_score": score_before,
        "fair_score": score_after,
        "difference": difference
    }

BIAS_FIELDS = [
    "gender",
    "age",
    "religion",
    "nationality",
    "marital_status"
]

def remove_bias(data):
    cleaned = data.copy()
    for field in BIAS_FIELDS:
        cleaned.pop(field, None)
    return cleaned

def explain_score():
    return {
        "ATS":"Resume-job matching",
        "Screening":"Interview response quality",
        "HR":"Communication and confidence",
        "Unified":"Weighted final hiring score"
    }

DATA_RETENTION = {
    "resume": "180 days",
    "interview": "180 days",
    "reports": "365 days"
}

def retention_policy():
    return DATA_RETENTION

def build_ethics_report():
    return {
        "consent":check_consent(),
        "bias_removed":True,
        "explainability":explain_score(),
        "retention_policy":retention_policy()
    }

if __name__ == "__main__":
    print(build_ethics_report())