# Screening Database Schema

## Candidates Table

candidate_id
name
email
phone

## Jobs Table

job_id
job_title
location

## Questions Table

question_id
category
question

## Transcripts Table

transcript_id
candidate_id
job_id
question_id
timestamp
transcript
confidence

## Screening Results Table

result_id
candidate_id
job_id
score
decision
