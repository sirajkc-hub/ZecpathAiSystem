SCORING_WEIGHTS = {
    "accuracy": 0.35,
    "depth": 0.25,
    "reasoning": 0.20,
    "real_world": 0.20
}

def accuracy_score(is_correct):
    if is_correct:
        return 1.0
    return 0.0

def depth_score(answer):
    words = len(answer.split())
    if words >= 80:
        return 1.0
    if words >= 40:
        return 0.75
    if words >= 20:
        return 0.50
    return 0.25

def reasoning_score(answer):
    keywords = [
        "because",
        "therefore",
        "first",
        "then",
        "finally"
    ]
    score = 0
    answer = answer.lower()
    for word in keywords:
        if word in answer:
            score += 1
    return score / len(keywords)

def real_world_score(answer):
    keywords = [
        "project",
        "production",
        "client",
        "real world",
        "deployment"
    ]
    score = 0
    answer = answer.lower()
    for word in keywords:
        if word in answer:
            score += 1
    return score / len(keywords)

def answer_quality(answer):
    words = len(answer.split())
    if words < 20:
        return "Shallow"
    if words < 60:
        return "Moderate"
    return "Deep"

def normalize_score(score, difficulty):
    factors = {
        "basic": 1.0,
        "intermediate": 0.95,
        "advanced": 0.90
    }
    return round(score * factors[difficulty], 2)

def technical_score(
        accuracy,
        depth,
        reasoning,
        real_world):
    score = (
        accuracy * SCORING_WEIGHTS["accuracy"] +
        depth * SCORING_WEIGHTS["depth"] +
        reasoning * SCORING_WEIGHTS["reasoning"] +
        real_world * SCORING_WEIGHTS["real_world"]
    )
    return round(score * 100, 2)

def build_technical_report(
        accuracy,
        depth,
        reasoning,
        real_world):
    return {
        "accuracy_score": accuracy,
        "depth_score": depth,
        "reasoning_score": reasoning,
        "real_world_score": real_world,
        "technical_score":
            technical_score(
                accuracy,
                depth,
                reasoning,
                real_world
            )
    }

if __name__ == "__main__":

    answer = """
    First I analyzed the issue.
    Because the API was slow,
    I optimized SQL queries
    and deployed the fix
    in production.
    """

    report = build_technical_report(
        accuracy_score(True),
        depth_score(answer),
        reasoning_score(answer),
        real_world_score(answer)
    )

    print(report)