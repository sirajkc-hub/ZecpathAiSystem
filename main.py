from parsers.pdf_reader import extract_pdf_text
from utils.text_cleaner import clean_text
from parsers.section_classifier import detect_sections

file_path = "data/Experienced_Python_Developer_Resume2.pdf"
raw_text = extract_pdf_text(file_path)
cleaned_text = clean_text(raw_text)
print(cleaned_text)

with open("outputs/cleaned_resume.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)
from parsers.jd_parser import *
jd_text = read_jd("data/sample_jd.txt")
cleaned_jd = clean_text(jd_text)
jd_object = build_jd_object(cleaned_jd)
print(jd_object)

import json
with open("outputs/jd_output.json", "w") as file:
    json.dump(jd_object, file, indent=4)

sections = detect_sections(raw_text)
print(sections)

import json
with open("outputs/resume_sections.json", "w") as file:
    json.dump(sections, file, indent=4)

from parsers.skill_extractor import *
skills = extract_skills(raw_text)
skills.extend(detect_skill_stack(raw_text))
skills = remove_duplicates(skills)
skill_output = build_skill_output(skills)
print(skill_output)

import json
with open("outputs/skills_output.json","w") as file:json.dump(skill_output,file,indent=4)

from parsers.experience_parser import *
experience_object = build_experience_object(raw_text)
print(experience_object)

total_exp = experience_object["total_experience"]
experience_score = min(total_exp / 24, 1)
print("Experience Score:", experience_score)

score = relevance_score("junior data scientist","data scientist")
print(score)

import json
with open("outputs/experience_output.json","w") as file:
    json.dump(experience_object,file,indent=4)

from parsers.education_parser import *
academic_profile = build_academic_profile(raw_text)
print(academic_profile)
if "computer science" in academic_profile["field"]:
    education_score = 1.0
else:
    education_score = 0.5
print("Education Score:", education_score)

score = education_relevance("computer science","data scientist")
print(score)

import json
with open("outputs/academic_profile.json","w") as file:
    json.dump(academic_profile,file,indent=4)



from parsers.semantic_matcher import *
resume_text = raw_text
jd_text = read_jd("data/sample_jd.txt")
similarity = semantic_similarity(resume_text,jd_text)
semantic_score = similarity
print("Semantic Score:", semantic_score)

skill_score = 0.90
experience_score = 0.85
project_score = 0.88
overall_score = overall_match_score(skill_score,experience_score,project_score)
print(overall_score)

import json
match_output = {"similarity_score":similarity,"match_type":classify_match(similarity)}
with open("outputs/match_output.json","w") as file:
    json.dump(match_output,file,indent=4)

from parsers.ats_scorer import *
jd_object = build_jd_object(cleaned_jd)
skill_output = build_skill_output(skills)
jd_skills = jd_object["skills"]
resume_skills = [item["skill"]for item in skill_output]
matched_skills = 0
for skill in jd_skills:
    if skill in resume_skills:
        matched_skills += 1
skill_score = matched_skills / len(jd_skills)
print("Skill Score:", skill_score)
candidate_score = generate_candidate_score(skill_score,experience_score,education_score,semantic_score,"python developer")
print("ATS SCORE:", candidate_score)

ats_output = {
    "candidate_id": "C001",
    "job_role": "Data Scientist",
    "skill_score": 0.90,
    "experience_score": 0.85,
    "education_score": 0.90,
    "semantic_score": 0.88,
    "final_ats_score": candidate_score
}

import json
with open("outputs/ats_score_output.json","w") as file:
    json.dump(ats_output,file,indent=4)

print(ats_output)

from parsers.candidate_ranker import *
ranked_candidates = rank_candidates(candidates)
ranked_candidates = shortlist_candidates(ranked_candidates)
print(ranked_candidates)

top_list = top_candidates(ranked_candidates)
print(top_list)

import json
with open("outputs/ranked_candidates.json","w") as file:
    json.dump(ranked_candidates,file,indent=4)

from parsers.fairness_engine import *
masked_resume = mask_personal_info(raw_text)
bias_flags = evaluate_bias(raw_text)
fair_ats_score = fair_score(candidate_score)
print(masked_resume)
print(bias_flags)
print(fair_ats_score)

fairness_output = {
    "bias_flags":bias_flags,
    "original_score":candidate_score,
    "normalized_score":fair_ats_score
}

import json
with open("outputs/fairness_report.json","w") as file:
    json.dump(fairness_output,file,indent=4)

del raw_text
del cleaned_text

from parsers.eligibility_engine import *
candidate_skills = [item["skill"]for item in skill_output]
candidate_exp = experience_object["total_experience"] / 12
role = "python developer"

decision = evaluate_candidate(candidate_score,candidate_skills,candidate_exp,role)
print(decision)

eligibility_result = {
    "candidate_id": "C001",
    "role": role,
    "ats_score": candidate_score,
    "decision": decision
}

import json
with open("outputs/eligibility_output.json","w") as file:
    json.dump(eligibility_result,file,indent=4)


