# Folder: backend/job_matcher.py

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def match_resume_to_job(resume, job_description):
    resume_text = ' '.join([resume.get('summary', ''), ' '.join(resume.get('skills', []))])
    embeddings = model.encode([resume_text, job_description])
    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()
    summary = f"Fit summary: Similarity score is {similarity:.2f}"
    return round(similarity * 100, 2), summary