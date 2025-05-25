# Folder: backend/resume_parser.py

import spacy

nlp = spacy.load('en_core_web_sm')

def parse_resume(resume_text):
    doc = nlp(resume_text)
    skills = [ent.text for ent in doc.ents if ent.label_ in ('SKILL', 'ORG', 'PRODUCT')]
    return {
        'summary': doc.text[:200],
        'skills': list(set(skills))
    }