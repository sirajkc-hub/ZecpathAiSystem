# ATS API Specification

## Resume Upload API

POST /api/v1/resume/upload

Response:
{
  "status": "success",
  "candidate_id": "C001"
}

## Resume Parsing API

POST /api/v1/resume/parse

Response:
{
  "skills": ["python", "sql"],
  "education": ["bsc"]
}

## ATS Scoring API

POST /api/v1/score

Response:
{
  "ats_score": 88.35
}

## Shortlisting API

POST /api/v1/shortlist

Response:
{
  "shortlisted": ["C001"]
}