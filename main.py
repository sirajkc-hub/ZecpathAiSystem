from parsers.pdf_reader import extract_pdf_text
from utils.text_cleaner import clean_text

file_path = "data/SIRAJ RESUME (1).pdf"

raw_text = extract_pdf_text(file_path)

cleaned_text = clean_text(raw_text)

print(cleaned_text)

with open("outputs/cleaned_resume.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)