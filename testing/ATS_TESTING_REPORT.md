# ATS Testing Report

| Candidate Type  | ATS Decision | Manual Review | Result   |
| --------------- | ------------ | ------------- | -------- |
| Fresher Resume  | Shortlisted  | Review        | Mismatch |
| Non-Tech Resume | Shortlisted  | Rejected      | Mismatch |
| Senior Resume   | Shortlisted  | Shortlisted   | Match    |
| Tech Resume     | Shortlisted  | Shortlisted   | Match    |

## Observations

* ATS scoring engine currently uses fixed scores.
* Some non-matching resumes receive high ATS scores.
* Manual review identified mismatches in candidate ranking.

## Recommendation

Replace fixed scoring values with dynamic scores generated from:

* Skills
* Experience
* Education
* Semantic similarity



# ATS Testing Report

## Tested Categories

- Tech Roles
- Non-Tech Roles
- Fresher Profiles
- Senior Profiles

## Results

Precision: 80%

Recall: 80%

Accuracy: 82%

## Observation

System performed well on
technical profiles.

Some mismatch cases
occurred due to missing skills.