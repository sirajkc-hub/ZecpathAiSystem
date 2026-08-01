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

role = "python developer"

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
    "job_role": role,
    "skill_score": skill_score,
    "experience_score": experience_score,
    "education_score": education_score,
    "semantic_score": semantic_score,
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

print("Candidate ID:", "C001")
print("ATS Score:", candidate_score)
screening_score = 92.5
confidence_score = 0.95
candidate_id = "C001"

print("Candidate ID:", candidate_id)
print("ATS Score:", candidate_score)
print("Screening Score:", screening_score)
print("Confidence Score:", confidence_score)
print("Final Decision:", decision)



#DAY 33
from parsers.hr_question_generator import *
role = "python developer"
experience = "fresher"
question = generate_question(
    role,
    experience
)
print("Role:", role)
print("Experience:", experience)
print("Interview Question:", question)
interview_output = {
    "candidate_id": "C001",
    "role": role,
    "experience": experience,
    "question": question
}
with open("outputs/interview_engine_output.json", "w") as file:
    json.dump(interview_output, file, indent=4)


#DAY 34
from parsers.followup_engine import *
candidate_answer = """
I worked on a resume parser project using Python.
"""
confidence_score = 0.95
followup = decide_followup(
    candidate_answer,
    confidence_score
)
print("Candidate Answer:")
print(candidate_answer)
print("\nConfidence Score:", confidence_score)
print("\nFollow-up Question:")
print(followup)
followup_output = {
    "candidate_answer": candidate_answer,
    "confidence_score": confidence_score,
    "followup_question": followup
}
with open("outputs/followup_output.json", "w") as file:
    json.dump(followup_output, file, indent=4)


#DAY 35
from parsers.aptitude_engine import *
answer = """
First I would identify the issue,
analyze logs,
implement the fix,
and verify the result.
"""
logical = logical_score(answer)
clarity = problem_solving_clarity(answer)
aptitude_report = build_aptitude_report(
    logical,
    clarity
)
print(aptitude_report)
with open("outputs/aptitude_report.json", "w") as file:
    json.dump(aptitude_report, file, indent=4)



#DAYY 36
from parsers.confidence_analyzer import *
candidate_response = """
I think I worked with Python.
Maybe I can solve this problem.
"""
confidence_report = build_confidence_object(candidate_response)
print(confidence_report)
with open("outputs/confidence_report.json", "w") as file:
    json.dump(confidence_report, file, indent=4)


#DAY 37
from parsers.communication_evaluator import *
candidate_response = """
I have worked on Django projects and developed REST APIs using Python.
"""
communication_report = build_communication_report(candidate_response)
print(communication_report)
with open("outputs/communication_report.json", "w") as file:
    json.dump(communication_report, file, indent=4)


#DAY 38
from parsers.unified_scoring_engine import *
candidate_id = "C001"
role = "python developer"
ats_score = candidate_score
screening_score = 92.5
hr_score = 88.0
candidate_report = build_candidate_object(
    candidate_id,
    role,
    ats_score,
    screening_score,
    hr_score
)
print(candidate_report)
with open("outputs/unified_candidate_report.json", "w") as file:
    json.dump(candidate_report, file, indent=4)



#DAY 39
from parsers.interview_summary import *
candidate_id = "C001"
hr_score = 88
communication_score = communication_report["communication_score"]
confidence_score = confidence_report["behavioral_confidence_score"]
consistency_score = 92
summary = build_summary(
    candidate_id,
    hr_score,
    communication_score,
    confidence_score,
    consistency_score
)
print(summary["report"])
with open("outputs/interview_summary.json", "w") as file:
    json.dump(summary, file, indent=4)


#DAY 42
from parsers.system_optimizer import *
ai_result = "Hire"
manual_result = "Hire"
prediction_status = evaluate_prediction(ai_result,manual_result)
followup_validation = validate_followup(candidate_answer)
normalized_score = normalize_score(candidate_score)
cleaned_answer = clean_transcript(candidate_answer)
optimization_report = build_optimization_report()

print("Prediction Validation :", prediction_status)
print("Follow-up Validation  :", followup_validation)
print("Normalized Score      :", normalized_score)
print("Cleaned Transcript    :", cleaned_answer)
print("\nOptimization Report")

for key, value in optimization_report.items():
    print(f"{key}: {value}")
system_optimizer_output = {
    "prediction_validation": prediction_status,
    "followup_validation": followup_validation,
    "normalized_score": normalized_score,
    "cleaned_transcript": cleaned_answer,
    "optimization_report": optimization_report
}

with open("outputs/system_optimizer_output.json", "w") as file:
    json.dump(system_optimizer_output, file, indent=4)


#DAY 43
from parsers.ethics_review import *
consent = check_consent()
fairness = fairness_review(
    candidate_score,
    fair_ats_score
)
candidate_data = {
    "name": "Arjun Menon",
    "gender": "Male",
    "age": 24,
    "religion": "None",
    "nationality": "Indian",
    "marital_status": "Single",
    "skills": ["Python", "Django", "SQL"]
}

bias_free_data = remove_bias(candidate_data)
score_explanation = explain_score()
retention = retention_policy()
ethics_report = build_ethics_report()
print("Consent:")
print(consent)
print("\nFairness Review:")
print(fairness)
print("\nBias-Free Candidate Data:")
print(bias_free_data)
print("\nScore Explainability:")
print(score_explanation)
print("\nRetention Policy:")
print(retention)
print("\nComplete Ethics Report:")
print(ethics_report)
ethics_output = {
    "consent": consent,
    "fairness_review": fairness,
    "bias_free_candidate": bias_free_data,
    "score_explanation": score_explanation,
    "retention_policy": retention,
    "ethics_report": ethics_report
}

with open("outputs/ethics_review_output.json", "w") as file:
    json.dump(ethics_output, file, indent=4)



#DAY 47
from parsers.technical_scoring_engine import *
technical_answer = """
First I analyzed the issue.
Because the API was slow,
I optimized SQL queries
and deployed the fix
in production.
"""

accuracy = accuracy_score(True)
depth = depth_score(technical_answer)
reasoning = reasoning_score(technical_answer)
real_world = real_world_score(technical_answer)

technical_report = build_technical_report(
    accuracy,
    depth,
    reasoning,
    real_world
)

difficulty = "intermediate"
technical_report["answer_quality"] = answer_quality(technical_answer)
technical_report["normalized_score"] = normalize_score(
    technical_report["technical_score"],
    difficulty
)
print(technical_report)
with open("outputs/technical_score_report.json", "w") as file:
    json.dump(technical_report, file, indent=4)

#DAY 48
from parsers.behavioral_mapper import *
signal = "stable_gaze"
insight = behavioral_insight(signal)
focus = 0.90
attention = 0.80
engagement = 0.80
behavior_score = behavioral_score(
    focus,
    attention,
    engagement
)

behavior_report = {
    "candidate_id": "C001",
    "signal": signal,
    "behavioral_insight": insight,
    "focus": focus,
    "attention": attention,
    "engagement": engagement,
    "behavioral_score": behavior_score
}

print(behavior_report)

with open("outputs/behavioral_report.json", "w") as file:
    json.dump(behavior_report, file, indent=4)


# DAY 49
from parsers.integrity_detector import *
events = [
    "tab_switching",
    "looking_away",
    "external_voice",
    "looking_away"
]
integrity_score = pattern_recognition(events)
integrity_report = build_integrity_report(
    "C001",
    integrity_score
)
print("Interview Events:")
print(events)
print("\nIntegrity Report:")
print(integrity_report)
with open("outputs/integrity_report.json", "w") as file:
    json.dump(integrity_report, file, indent=4)


# ==========================================================
# DAY 50 - MACHINE TEST EVALUATOR
# ==========================================================

from parsers.machine_test_evaluator import *

print("\n================ DAY 50 : MACHINE TEST EVALUATOR ================\n")

# Candidate Submission
candidate_id = "C001"

code_snapshot = """
def add(a, b):
    return a + b
"""

execution_result = "Success"

submission = build_submission_object(
    candidate_id,
    code_snapshot,
    execution_result
)

# Machine Test Evaluation
correctness = 1.0
efficiency = 0.80
code_quality = 0.90
problem_solving = 0.85

machine_test_score = calculate_machine_test_score(
    correctness,
    efficiency,
    code_quality,
    problem_solving
)

time_taken = 42

machine_test_report = build_machine_test_report(
    candidate_id,
    machine_test_score,
    time_taken
)

print("Submission:")
print(submission)

print("\nMachine Test Report:")
print(machine_test_report)

machine_test_output = {
    "submission": submission,
    "report": machine_test_report
}

with open("outputs/machine_test_report.json", "w") as file:
    json.dump(machine_test_output, file, indent=4)



# DAY 50

from parsers.machine_test_evaluator import *
candidate_id = "C001"
code_snapshot = """
def add(a, b):
    return a + b"""
execution_result = "Success"
submission = build_submission_object(
    candidate_id,
    code_snapshot,
    execution_result
)
correctness = 1.0
efficiency = 0.80
code_quality = 0.90
problem_solving = 0.85
machine_test_score = calculate_machine_test_score(
    correctness,
    efficiency,
    code_quality,
    problem_solving
)
time_taken = 42
machine_test_report = build_machine_test_report(
    candidate_id,
    machine_test_score,
    time_taken
)
print("Submission:")
print(submission)
print("\nMachine Test Report:")
print(machine_test_report)
machine_test_output = {
    "submission": submission,
    "report": machine_test_report
}
with open("outputs/machine_test_report.json", "w") as file:
    json.dump(machine_test_output, file, indent=4)


#DAY 51

from parsers.cross_round_aggregation import *
candidate_id = "C001"
role = "python developer"
ats = candidate_score
screening = screening_score
hr = hr_score
technical = technical_report["technical_score"]
machine_test = machine_test_report["machine_test_score"]
candidate_score_report = build_candidate_score(
    candidate_id,
    role,
    ats,
    screening,
    hr,
    technical,
    machine_test
)

print(candidate_score_report)
with open("outputs/hiring_fit_report.json", "w") as file:
    json.dump(candidate_score_report, file, indent=4)


# DAY 52
from parsers.final_recommendation_ai import *
candidate_id = "C001"
hiring_fit_score = candidate_score_report["hiring_fit_score"]
behavioral_score = behavior_report["behavioral_score"]
integrity_score = integrity_report["integrity_score"]
decision_report = build_decision_output(
    candidate_id,
    hiring_fit_score,
    behavioral_score,
    integrity_score
)
print(decision_report)
with open("outputs/final_decision_output.json", "w") as file:
    json.dump(decision_report, file, indent=4)



# DAY 53
from parsers.hiring_report_generator import *
candidate_id = "C001"
ats_score = candidate_score
screening_score = screening_score
hr_score = hr_score
technical_score = technical_report["technical_score"]
behavioral_score = behavior_report["behavioral_score"]
integrity_score = integrity_report["integrity_score"]
hiring_fit_score = candidate_score_report["hiring_fit_score"]
confidence_score = decision_report["confidence_score"]
hiring_report = build_hiring_report(
    candidate_id,
    ats_score,
    screening_score,
    hr_score,
    technical_score,
    behavioral_score,
    integrity_score,
    hiring_fit_score,
    confidence_score
)
print(hiring_report)
with open("outputs/hiring_intelligence_report.json", "w") as file:
    json.dump(hiring_report, file, indent=4)


# DAY 54
from parsers.optimization_refinement import *
import time
start_time = time.time()
predicted = [
    "Hire",
    "Reject",
    "Hire",
    "Review"
]
actual = [
    "Hire",
    "Hire",
    "Reject",
    "Review"
]
prediction_analysis = analyze_predictions(
    predicted,
    actual
)

refined_decision = refine_threshold(
    candidate_score_report["hiring_fit_score"]
)

intent_result = detect_intent(
    candidate_answer
)

consistency = consistency_check(
    candidate_score,
    technical_report["technical_score"],
    hr_score
)

execution_time = processing_speed(
    start_time
)

optimization_report = build_optimization_report()

print("Prediction Analysis:")
print(prediction_analysis)

print("\nRefined Decision:")
print(refined_decision)

print("\nIntent Detection:")
print(intent_result)

print("\nConsistency Check:")
print(consistency)

print("\nProcessing Time:")
print(execution_time, "seconds")

print("\nOptimization Report:")
print(optimization_report)

optimization_output = {
    "prediction_analysis": prediction_analysis,
    "refined_decision": refined_decision,
    "intent_detection": intent_result,
    "consistency": consistency,
    "processing_time_seconds": execution_time,
    "optimization_report": optimization_report
}

with open("outputs/optimization_report.json", "w") as file:
    json.dump(optimization_output, file, indent=4)


#DAY 55
from parsers.security_governance import *
audit = audit_log(
    "C001",
    "ATS",
    "Score Generated",
    candidate_score
)

decision = decision_log(
    "C001",
    decision_report["recommendation"],
    decision_report["confidence_score"]
)

governance = build_governance_report()

print("Audit Log:")
print(audit)

print("\nDecision Log:")
print(decision)

print("\nRetention Policy:")
print(retention_policy())

print("\nConsent Verification:")
print(verify_consent())

print("\nSecure Storage:")
print(storage_plan())

print("\nAdmin Access:")
print(access_control("admin"))

print("\nGovernance Report:")
print(governance)

governance_output = {
    "audit_log": audit,
    "decision_log": decision,
    "retention_policy": retention_policy(),
    "consent": verify_consent(),
    "storage": storage_plan(),
    "access": access_control("admin"),
    "governance_report": governance
}

with open("outputs/governance_report.json", "w") as file:
    json.dump(governance_output, file, indent=4)



#DAY 56
from parsers.full_system_simulation import *
resume = resume_stage()
ats = ats_stage(candidate_score)
screening = screening_stage(screening_score)
hr = hr_stage(hr_score)
technical = technical_stage(
    technical_report["technical_score"]
)
final = final_stage(
    decision_report["recommendation"]
)
comparison = compare_ai_human(
    decision_report["recommendation"],
    "Selected"      # Sample human decision
)
consistency = inconsistency_check(
    candidate_score,
    hr_score,
    technical_report["technical_score"]
)
system_report = build_system_report()
simulation_output = {
    "resume_stage": resume,
    "ats_stage": ats,
    "screening_stage": screening,
    "hr_stage": hr,
    "technical_stage": technical,
    "final_stage": final,
    "ai_vs_human": comparison,
    "consistency": consistency,
    "system_report": system_report
}
print(simulation_output)
with open("outputs/system_simulation_report.json", "w") as file:
    json.dump(simulation_output, file, indent=4)



#DAY 57

from parsers.debugging_stabilization import *
validated_score = validate_score(candidate_score)

conversation_status = validate_conversation(
    question,
    candidate_answer
)

pipeline_status = validate_pipeline({
    "candidate_id": "C001",
    "ats_score": candidate_score,
    "technical_score": technical_report["technical_score"],
    "recommendation": decision_report["recommendation"]
})

division_result = safe_division(10, 0)

api_status = validate_api_output(decision_report)

edge_case = edge_case_check({
    "candidate_id": "C001",
    "ats_score": candidate_score
})

debug_report = build_debug_report()

print("Validated Score:", validated_score)
print("Conversation:", conversation_status)
print("Pipeline Missing Fields:", pipeline_status)
print("Safe Division:", division_result)
print("API Validation:", api_status)
print("Edge Case:", edge_case)
print("Debug Report:", debug_report)

debug_output = {
    "validated_score": validated_score,
    "conversation_status": conversation_status,
    "pipeline_validation": pipeline_status,
    "safe_division": division_result,
    "api_validation": api_status,
    "edge_case": edge_case,
    "debug_report": debug_report
}

with open("outputs/debugging_report.json", "w") as file:
    json.dump(debug_output, file, indent=4)

