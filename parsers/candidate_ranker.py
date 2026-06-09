candidates = [

    {
        "candidate_id": "C001",
        "name": "Siraj",
        "ats_score": 88.35
    },
    {
        "candidate_id": "C002",
        "name": "Arjun",
        "ats_score": 75.20
    },
    {
        "candidate_id": "C003",
        "name": "Rahul",
        "ats_score": 62.50
    },
    {
        "candidate_id": "C004",
        "name": "Akhil",
        "ats_score": 45.00
    }
]

def rank_candidates(candidates):
    return sorted(candidates,key=lambda x: x["ats_score"],reverse=True)

SHORTLIST_THRESHOLD = 80
REVIEW_THRESHOLD = 60

def candidate_status(score):
    if score >= SHORTLIST_THRESHOLD:
        return "Shortlisted"
    elif score >= REVIEW_THRESHOLD:
        return "Review"
    return "Rejected"

def shortlist_candidates(candidates):
    for candidate in candidates:
        candidate["status"] = candidate_status(candidate["ats_score"])
    return candidates

def top_candidates(candidates,top_n=3):
    ranked = rank_candidates(candidates)
    return ranked[:top_n]

def recruiter_view(candidates):
    output = []
    for candidate in candidates:
        output.append({
            "candidate_id":candidate["candidate_id"],
            "name":candidate["name"],
            "ats_score":candidate["ats_score"],
            "status":candidate["status"]
        })
    return output