def generate_question(role, experience):
    if role == "python developer":
        if experience == "fresher":
            return "Explain a Python project you have worked on."
        return "Describe your experience with Django and REST APIs."
    if role == "data scientist":
        if experience == "fresher":
            return "Which machine learning algorithms have you used?"
        return "Tell me about a machine learning model you deployed."
    return "Can you tell me about yourself?"



