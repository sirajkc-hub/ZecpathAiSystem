SECTION_HEADINGS = {
    "skills": ["skills", "technical skills", "core skills"],
    "experience": ["experience", "work experience", "employment history"],
    "education": ["education", "academic background"],
    "certifications": ["certifications", "certificates"],
    "projects": ["projects", "academic projects"]
}
skills_keywords = [
    "python",
    "sql",
    "java",
    "power bi"
]

def detect_sections(text):
    lines = text.split("\n")
    detected_sections = {}
    current_section = "general"
    detected_sections[current_section] = []
    for line in lines:
        clean_line = line.strip().lower()
        found = False
        for section, headings in SECTION_HEADINGS.items():
            if clean_line in headings:
                current_section = section
                detected_sections[current_section] = []
                found = True
                break
        if not found:
            detected_sections[current_section].append(line)
    return detected_sections

