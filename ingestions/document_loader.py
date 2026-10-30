import pandas as pd
from pypdf import PdfReader

def load_pdf(file):
    text = ""
    pdf = PdfReader(file)
    for page in pdf.pages:
        text += page.extract_text()
    return text

def load_txt(file):
    return file.read().decode("utf-8")

def load_csv(file):
    df = pd.read_csv(file)
    return df.to_string()

def load_excel(file):
    df = pd.read_excel(file)
    return df.to_string()