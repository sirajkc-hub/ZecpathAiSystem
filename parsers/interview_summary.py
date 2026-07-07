def extract_strengths(hr_score, communication_score):
    strengths = []
    if hr_score >= 80:
        strengths.append("Strong HR performance")
    if communication_score >= 80:
        strengths.append("Good communication skills")
    return strengths

def extract_weaknesses(confidence_score):
    weaknesses = []
    if confidence_score < 60:
        weaknesses.append("Low confidence")
    return weaknesses

def cultural_fit_indicator(hr_score):
    if hr_score >= 75:
        return "Good Cultural Fit"
    return "Needs Further Evaluation"

def risk_flags(consistency_score):
    risks = []
    if consistency_score < 60:
        risks.append("Inconsistent responses")
    return risks

def highlight_inconsistency(consistency_score):
    if consistency_score < 60:
        return "Potential inconsistency detected."
    return "No major inconsistencies."

def overall_hr_performance(hr_score):
    if hr_score >= 85:
        return "Excellent"
    if hr_score >= 70:
        return "Good"
    return "Average"

def generate_report(summary):
    strengths = "\n".join(summary["strengths"]) if summary["strengths"] else "None"
    weaknesses = "\n".join(summary["weaknesses"]) if summary["weaknesses"] else "None"
    risk_flags = "\n".join(summary["risk_flags"]) if summary["risk_flags"] else "None"
    return f"""
Candidate Summary
Strengths:
{strengths}
Weaknesses:
{weaknesses}
Cultural Fit:
{summary['cultural_fit']}
Risk Flags:
{risk_flags}
Overall Performance:
{summary['overall_performance']}
"""

def build_summary(
        candidate_id,
        hr_score,
        communication_score,
        confidence_score,
        consistency_score):
    summary = {
        "candidate_id": candidate_id,
        "strengths":extract_strengths(hr_score,communication_score),
        "weaknesses":extract_weaknesses(confidence_score),
        "cultural_fit":cultural_fit_indicator(hr_score),
        "risk_flags":risk_flags(consistency_score),
        "overall_performance":overall_hr_performance(hr_score)
    }
    summary["report"] = generate_report(summary)
    return summary

if __name__ == "__main__":
    result = build_summary(
        "C001",
        88,
        90,
        85,
        92
    )
    print(result)