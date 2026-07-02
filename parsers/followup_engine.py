def is_incomplete(answer):
    return len(answer.split()) < 5

VAGUE_WORDS = [
    "maybe",
    "not sure",
    "i think",
    "possibly"
]
def is_vague(answer):
    answer = answer.lower()
    for word in VAGUE_WORDS:
        if word in answer:
            return True
    return False

def clarification_trigger():
    return (
        "Could you explain that in more detail?"
    )

def deepening_trigger():
    return (
        "Can you tell me more about "
        "your approach?"
    )

def example_prompt():
    return (
        "Can you give an example "
        "from your experience?"
    )

def difficulty_adaptation(
        confidence_score):
    if confidence_score > 0.90:
        return (
            "How would you solve this "
            "in a production system?"
        )
    return ("Can you explain the basics?")

asked_questions = []
def already_asked(question):
    return question in asked_questions
def store_question(question):
    asked_questions.append(question)

conversation_state = {
    "current_question": None,
    "question_count": 0,
    "followups_used": 0
}

def decide_followup(
        answer,
        confidence_score):
    if is_incomplete(answer):
        return clarification_trigger()
    if is_vague(answer):
        return example_prompt()
    if confidence_score > 0.90:
        return difficulty_adaptation(
            confidence_score
        )
    return deepening_trigger()

if __name__ == "__main__":
    answer = ("I worked with Python.")
    result = decide_followup(
        answer,
        0.95
    )
    print(result)
