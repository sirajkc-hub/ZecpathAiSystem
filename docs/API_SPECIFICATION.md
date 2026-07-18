# API Specification

## Resume Upload

POST /resume/upload

Input

```json
{
  "resume":"PDF File"
}
```

Output

```json
{
  "candidate_id":"C001",
  "ats_score":90.5
}
```

---

## AI Screening

POST /screening/start

Input

```json
{
  "candidate_id":"C001"
}
```

Output

```json
{
  "question":"Tell me about yourself"
}
```

---

## HR Interview

POST /interview/evaluate

Input

```json
{
  "candidate_id":"C001",
  "answer":"..."
}
```

Output

```json
{
  "hr_score":88
}
```

---

## Final Hiring Decision

GET /candidate/result/C001

Output

```json
{
  "ats_score":90,
  "screening_score":89,
  "hr_score":91,
  "final_score":90,
  "recommendation":"Hire"
}
```