IDEAL_STRUCTURE = {
    "problem_identification": 0.25,
    "analysis": 0.25,
    "solution": 0.30,
    "verification": 0.20
}

def logical_score(answer):
    keywords = [
        "because",
        "therefore",
        "if",
        "then",
        "solution"
    ]
    score = 0
    answer = answer.lower()
    for word in keywords:
        if word in answer:
            score += 1
    return score / len(keywords)

def problem_solving_clarity(answer):
    indicators = [
        "identify",
        "analyze",
        "implement",
        "verify"
    ]
    count = 0
    answer = answer.lower()
    for item in indicators:
        if item in answer:
            count += 1
    return count / len(indicators)

def aptitude_score(logical,clarity):
    score = (logical * 0.60 +clarity * 0.40)
    return round(score * 100,2)

def build_aptitude_report(logical,clarity):
    return {
        "logical_reasoning_score":logical,
        "problem_solving_clarity":clarity,
        "final_aptitude_score":aptitude_score(logical,clarity)
    }

if __name__ == "__main__":
    answer = """
    First I would identify the issue,
    analyze logs,
    implement the fix,
    and verify the result.
    """
    logical = logical_score(answer)
    clarity = problem_solving_clarity(answer)
    print(build_aptitude_report(logical,clarity))
