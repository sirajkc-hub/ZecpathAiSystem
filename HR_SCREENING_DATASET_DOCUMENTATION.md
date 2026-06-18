# HR Screening Dataset Documentation

## Purpose

This dataset is designed to support AI-powered HR screening and candidate evaluation.

The dataset contains structured screening questions that can be used by future AI interview agents and recruitment systems.

---

## Question Categories

* INTRODUCTION
* EDUCATION
* EXPERIENCE
* SKILLS
* LOCATION
* SALARY
* NOTICE_PERIOD

---

## Answer Types

Supported answer types:

* text
* number
* yes_no

---

## Mandatory Questions

Mandatory questions must be answered by the candidate.

Example:

* Introduction
* Skills
* Experience
* Education

---

## Importance Scores

Importance scores indicate the significance of a question during candidate evaluation.

Scale:

* 5 = Very Important
* 4 = Important
* 3 = Moderate
* 2 = Optional
* 1 = Low Priority

---

## AI Conversation Ready Structure

Each question object contains:

* question_id
* role
* category
* question
* answer_type
* mandatory
* importance

This structure allows future AI interview agents to ask and evaluate questions automatically.

---

## Multilingual Support

The dataset supports multilingual questions.

Example:

* question_en
* question_ml

This enables future AI interview systems to communicate with candidates in their preferred language.

---

## Future Enhancements

* Additional job roles
* More screening questions
* Hindi and Arabic language support
* AI-based answer evaluation
* Dynamic interview question generation
