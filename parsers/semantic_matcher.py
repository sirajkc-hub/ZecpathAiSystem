from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embedding(text):
    return model.encode(text)

from sentence_transformers import util

def semantic_similarity(resume_text,jd_text):
    resume_embedding = generate_embedding(resume_text)
    jd_embedding = generate_embedding(jd_text)
    score = util.cos_sim(resume_embedding,jd_embedding)
    return float(score)

def compare_skills(resume_skills,jd_skills):
    resume_text = " ".join(resume_skills)
    jd_text = " ".join(jd_skills)
    return semantic_similarity(resume_text,jd_text)

def compare_experience(resume_exp,jd_exp):
    return semantic_similarity(resume_exp,jd_exp)

def compare_projects(resume_projects,jd_projects):
    return semantic_similarity(resume_projects,jd_projects)

def overall_match_score(skill_score,exp_score,project_score):
    return round((skill_score + exp_score + project_score)/3,2)

def classify_match(score):
    if score >= 0.80:
        return "Strong Match"
    elif score >= 0.60:
        return "Moderate Match"
    return "Weak Match"