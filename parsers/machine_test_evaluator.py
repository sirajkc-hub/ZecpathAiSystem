METRIC_WEIGHTS = {
    "correctness": 0.40,
    "efficiency": 0.25,
    "code_quality": 0.20,
    "problem_solving": 0.15
}
def calculate_machine_test_score(
        correctness,
        efficiency,
        code_quality,
        problem_solving):
    score = (
        correctness * METRIC_WEIGHTS["correctness"]
        +
        efficiency * METRIC_WEIGHTS["efficiency"]
        +
        code_quality * METRIC_WEIGHTS["code_quality"]
        +
        problem_solving * METRIC_WEIGHTS["problem_solving"]
    )
    return round(score * 100, 2)
def build_submission_object(
        candidate_id,
        code_snapshot,
        execution_result):
    return {
        "candidate_id": candidate_id,
        "code_snapshot": code_snapshot,
        "execution_result": execution_result
    }

def time_score(minutes_taken):
    if minutes_taken <= 30:
        return 1.0
    if minutes_taken <= 60:
        return 0.8
    return 0.6

def build_machine_test_report(
        candidate_id,
        score,
        time_taken):
    return {
        "candidate_id": candidate_id,
        "machine_test_score": score,
        "time_taken": time_taken,
        "status":
            "Passed"
            if score >= 70
            else "Needs Improvement"
    }

if __name__ == "__main__":
    score = calculate_machine_test_score(
        1.0,
        0.8,
        0.9,
        0.85
    )
    report = build_machine_test_report(
        "C001",
        score,
        42
    )
    print(report)