CONVERSATION_STATES = [
    "START",
    "ASK_QUESTION",
    "WAIT_FOR_ANSWER",
    "PROCESS_ANSWER",
    "FOLLOW_UP",
    "NEXT_QUESTION",
    "END"
]

def next_state(current_state):
    flow = {
        "START": "ASK_QUESTION",
        "ASK_QUESTION": "WAIT_FOR_ANSWER",
        "WAIT_FOR_ANSWER": "PROCESS_ANSWER",
        "PROCESS_ANSWER": "NEXT_QUESTION",
        "NEXT_QUESTION": "ASK_QUESTION"
    }
    return flow.get(current_state, "END")

def handle_silence():
    return "I couldn't hear your response. Could you please repeat it?"

def handle_confusion():
    return "No problem. Let me explain the question differently."

def handle_repeated_answer():
    return "You already mentioned that. Let's move to the next question."

FALLBACK_QUESTIONS = [
    "Could you explain that in more detail?",
    "Can you provide an example?",
    "Could you clarify your answer?"
]

def follow_up_trigger(answer):
    answer = answer.lower()
    if "python" in answer:
        return "Can you describe a Python project you worked on?"
    if "django" in answer:
        return "How did you use Django in that project?"
    return None

def retry_question():
    return "Let's try that question once again."

def build_conversation_state(state):
    return {"state": state,"next_state": next_state(state)}

if __name__ == "__main__":

    print(build_conversation_state("START"))

    print(handle_silence())

    print(handle_confusion())

    print(follow_up_trigger("I have worked in Python."))

