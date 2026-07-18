import json

with open("datasets/demo_candidates.json") as file:
    candidates = json.load(file)

for candidate in candidates:
    print("=" * 50)
    print("Candidate :", candidate["name"])
    print("Role :", candidate["role"])
    print("ATS Score :", candidate["ats_score"])
    print("Screening Score :", candidate["screening_score"])
    print("HR Score :", candidate["hr_score"])
    print("Final Score :", candidate["final_score"])
    print("Recommendation :", candidate["recommendation"])

