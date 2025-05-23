
from flask import Flask, request, jsonify
from resume_parser import parse_resume
from job_matcher import match_resume_to_job

app = Flask(__name__)

@app.route('/match', methods=['POST'])
def match():
    resume_text = request.json.get('resume')
    job_description = request.json.get('job_description')

    parsed_resume = parse_resume(resume_text)
    match_score, summary = match_resume_to_job(parsed_resume, job_description)

    return jsonify({
        'match_score': match_score,
        'summary': summary,
        'skills': parsed_resume.get('skills', [])
    })

if __name__ == '__main__':
    app.run(debug=True)