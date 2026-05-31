import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[•●▪]', '-', text)
    text = re.sub(r'[^\w\s\n-]', '', text)
    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines]
    return "\n".join(cleaned_lines)