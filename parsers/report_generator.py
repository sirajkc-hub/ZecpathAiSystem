def generate_screening_report(
        candidate_id,
        candidate_name,
        ats_score,
        screening_score,
        confidence_score,
        skills,
        availability,
        salary,
        strengths,
        risks,
        missing_data):
    return {
        "candidate_id": candidate_id,
        "candidate_name": candidate_name,
        "ats_score": ats_score,
        "screening_score": screening_score,
        "confidence_score": confidence_score,
        "skills_confirmed": skills,
        "availability": availability,
        "salary_expectation": salary,
        "strengths": strengths,
        "risks": risks,
        "missing_data": missing_data
    }

def summarize_answers():
    return [
        "2 years Python experience",
        "Immediate availability",
        "Expected salary 8 LPA"
    ]

def identify_strengths():
    return ["Strong Python knowledge","Django experience","Immediate joining"]
def identify_risks():
    return ["Limited leadership experience"]
def detect_missing_data():
    return ["Notice period not provided"]

def build_recruiter_report():
    report = generate_screening_report(
        candidate_id="C001",
        candidate_name="Arjun Menon",
        ats_score=90.66,
        screening_score=92.50,
        confidence_score=0.95,
        skills=[
            "Python",
            "SQL",
            "Django"
        ],
        availability="Immediate",
        salary="8 LPA",
        strengths=identify_strengths(),
        risks=identify_risks(),
        missing_data=detect_missing_data()
    )
    report["key_answers"] = summarize_answers()
    return report

if __name__ == "__main__":
    report = build_recruiter_report()
    print(report)

