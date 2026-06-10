import re

def clean_text(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[•●▪]', ' ', text)
    text = re.sub(r'[_\-]{2,}', ' ', text)
    return text.strip()