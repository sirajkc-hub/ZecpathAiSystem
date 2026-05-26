from parsers.pdf_reader import extract_pdf_text

def test_pdf_extraction():

    text = extract_pdf_text("data/SIRAJ RESUME (1).pdf")

    assert len(text) > 0