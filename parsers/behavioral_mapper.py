SIGNAL_MAPPING = {
    "stable_gaze":"High Focus",
    "frequent_head_turn":"Possible Distraction",
    "consistent_attention":"Good Engagement",
    "frequent_fidgeting":"Possible Nervousness"
}
def behavioral_insight(signal):
    return SIGNAL_MAPPING.get(signal,"Unknown")

BEHAVIOR_WEIGHTS = {

    "focus": 0.40,

    "attention": 0.35,

    "engagement": 0.25
}


def behavioral_score(
        focus,
        attention,
        engagement):
    score = (
        focus * BEHAVIOR_WEIGHTS["focus"]
        +
        attention * BEHAVIOR_WEIGHTS["attention"]
        +
        engagement * BEHAVIOR_WEIGHTS["engagement"]
    )
    return round(score * 100, 2)

if __name__ == "__main__":
    print(behavioral_insight("stable_gaze"))
    print(behavioral_score(0.9,0.8,0.8))