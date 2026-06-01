TECH_SKILLS = [
    "python",
    "java",
    "sql",
    "django",
    "flask",
    "fastapi",
    "power bi",
    "excel",
    "tensorflow",
    "pandas",
    "numpy"
]
BUSINESS_SKILLS = [
    "leadership",
    "communication",
    "teamwork",
    "project management"
]
CREATIVE_SKILLS = [
    "photoshop",
    "illustrator",
    "figma",
    "canva"
]

MASTER_SKILLS = (
    TECH_SKILLS +
    BUSINESS_SKILLS +
    CREATIVE_SKILLS
)

def extract_skills(text):
    found_skills = []
    text = text.lower()
    for skill in MASTER_SKILLS:
        if skill in text:
            found_skills.append(skill)
    return found_skills

SKILL_SYNONYMS = {
    "py": "python",
    "ml": "machine learning",
    "js": "javascript",
    "postgres": "postgresql"
}

def normalize_skill(skill):
    return SKILL_SYNONYMS.get(skill, skill)

SKILL_STACKS = {
    "mern": [
        "mongodb",
        "express",
        "react",
        "nodejs"
    ],

    "mean": [
        "mongodb",
        "express",
        "angular",
        "nodejs"
    ]
}

def detect_skill_stack(text):
    found = []
    for stack in SKILL_STACKS:
        if stack in text.lower():
            found.extend(SKILL_STACKS[stack])
    return found

SPELLING_VARIATIONS = {
    "powerbi": "power bi",
    "node.js": "nodejs"
}

def remove_duplicates(skills):
    return list(set(skills))


def confidence_score(skill):
    scores = {
        "python": 0.95,
        "sql": 0.90,
        "power bi": 0.92
    }
    return scores.get(skill, 0.80)

def build_skill_output(skills):
    result = []
    for skill in skills:
        result.append({
            "skill": skill,
            "confidence": confidence_score(skill)
        })
    return result