SIGNAL_THRESHOLDS = {
    "tab_switching": 3,
    "screen_focus_loss": 2,
    "external_voice": 1,
    "looking_away": 5
}
def detect_flag(signal, count):
    threshold = SIGNAL_THRESHOLDS.get(signal)
    if threshold is None:
        return False
    return count >= threshold

def pattern_recognition(events):
    suspicious_patterns = [
        "tab_switching",
        "external_voice",
        "looking_away"
    ]
    count = 0
    for event in events:
        if event in suspicious_patterns:
            count += 1
    return count

def warning_level(score):
    if score >= 5:
        return "High"
    if score >= 3:
        return "Medium"
    return "Low"

def interview_risk(score):
    if score >= 5:
        return "High Risk"
    if score >= 3:
        return "Moderate Risk"
    return "Low Risk"

def build_integrity_report(
        candidate_id,
        integrity_score):
    return {
        "candidate_id": candidate_id,
        "integrity_score": integrity_score,
        "warning_level":
            warning_level(
                integrity_score
            ),
        "risk_tag":
            interview_risk(
                integrity_score
            )
    }

if __name__ == "__main__":
    events = [
        "tab_switching",
        "looking_away",
        "external_voice",
        "looking_away"
    ]
    integrity_score = pattern_recognition(events)
    report = build_integrity_report(
        "C001",
        integrity_score
    )
    print(report)

