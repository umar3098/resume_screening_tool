# Folder: test/test_resume_parser.py

from backend.resume_parser import parse_resume

def test_resume_parser():
    resume = "Expert in Python and cloud services like AWS."
    result = parse_resume(resume)
    assert 'Python' in result['summary']
    assert isinstance(result['skills'], list)