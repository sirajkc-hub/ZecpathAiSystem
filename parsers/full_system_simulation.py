def resume_stage():
    return {
        "stage": "Resume Upload",
        "status": "Completed"
    }

def resume_stage():
    return {
        "stage": "Resume Upload",
        "status": "Completed"
    }

def ats_stage(score):
    return {
        "stage": "ATS Scoring",
        "score": score,
        "status": "Completed"
    }

def screening_stage(score):
    return {
        "stage": "Screening",
        "score": score,
        "status": "Completed"
    }

def hr_stage(score):
    return {
        "stage": "HR Interview",
        "score": score,
        "status": "Completed"
    }

def technical_stage(score):
    return {
        "stage": "Technical Interview",
        "score": score,
        "status": "Completed"
    }

def final_stage(recommendation):
    return {
        "stage": "Final Decision",
        "recommendation": recommendation,
        "status": "Completed"
    }

def compare_ai_human(ai_decision, human_decision):
    return {
        "ai_decision": ai_decision,
        "human_decision": human_decision,
        "match": ai_decision == human_decision
    }

def inconsistency_check(ats, hr, technical):
    values = [ats, hr, technical]
    difference = max(values) - min(values)
    return difference <= 15

def build_system_report():
    return {
        "pipeline_completed": True,
        "resume_processed": True,
        "ats_completed": True,
        "screening_completed": True,
        "hr_completed": True,
        "technical_completed": True,
        "final_decision_generated": True,
        "system_status": "Success"
    }

if __name__ == "__main__":
    print(resume_stage())
    print(ats_stage(88.35))
    print(screening_stage(86))
    print(hr_stage(84))
    print(technical_stage(91))
    print(final_stage("Selected"))
    print(compare_ai_human("Selected", "Selected"))
    print(inconsistency_check(88, 84, 91))
    print(build_system_report())