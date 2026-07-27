def ats_summary(ats_score):
    if ats_score >= 85:
        return "Excellent Resume Match"
    if ats_score >= 70:
        return "Good Resume Match"
    return "Needs Improvement"

def candidate_insights(technical_score,behavioral_score):
    strengths = []
    weaknesses = []
    if technical_score >= 80:
        strengths.append("Strong Technical Skills")
    else:
        weaknesses.append("Technical Skills Need Improvement")
    if behavioral_score >= 80:
        strengths.append("Good Communication")
    else:
        weaknesses.append("Behavioral Improvement Required")
    return strengths, weaknesses

def risk_indicators(integrity_score,confidence_score):
    risks = []
    if integrity_score < 70:
        risks.append("Integrity Risk")
    if confidence_score < 0.75:
        risks.append("Low Decision Confidence")
    return risks

def final_recommendation(
        hiring_fit_score):
    if hiring_fit_score >= 85:
        return "Selected"
    if hiring_fit_score >= 65:
        return "Hold / Review"
    return "Rejected"

def build_hiring_report(
        candidate_id,
        ats_score,
        screening_score,
        hr_score,
        technical_score,
        behavioral_score,
        integrity_score,
        hiring_fit_score,
        confidence_score):
    strengths, weaknesses = candidate_insights(technical_score,behavioral_score)
    return {
        "candidate_id": candidate_id,
        "ats_summary":ats_summary(ats_score),
        "screening_score":screening_score,
        "hr_score":hr_score,
        "technical_score":technical_score,
        "behavioral_score":behavioral_score,
        "strengths":strengths,
        "weaknesses":weaknesses,
        "risk_indicators":risk_indicators(integrity_score,confidence_score),
        "recommendation":final_recommendation(hiring_fit_score)
    }

if __name__ == "__main__":
    report = build_hiring_report(
        "C001",
        90,
        88,
        86,
        91,
        84,
        92,
        89,
        0.95
    )
    print(report)
