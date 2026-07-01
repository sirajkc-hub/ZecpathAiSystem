INTERVIEW_PHASES = [
    "INTRODUCTION",
    "CORE_HR",
    "ROLE_EVALUATION",
    "CLOSING"
]

def build_interview_state():
    return {
        "current_phase": "INTRODUCTION",
        "question_count": 0,
        "completed": False
    }

def next_phase(current_phase):
    flow = {
        "INTRODUCTION": "CORE_HR",
        "CORE_HR": "ROLE_EVALUATION",
        "ROLE_EVALUATION": "CLOSING",
        "CLOSING": "END"
    }
    return flow.get(current_phase, "END")

