# Folder: test/test_job_parser.py

from backend.job_matcher import match_resume_to_job

def test_job_match():
    resume = {'summary': 'Python developer', 'skills': ['Python', 'Flask']}
    job_desc = "Looking for a Python and Flask developer"
    score, summary = match_resume_to_job(resume, job_desc)
    assert isinstance(score, float)
    assert "Similarity" in summary