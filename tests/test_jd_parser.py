from parsers.jd_parser import *

def test_skill_extraction():

    sample_text = "python sql django"

    skills = extract_skills(sample_text)

    assert "python" in skills