# Intelligent Resume Screening Tool

# Folder: frontend/app.py

import streamlit as st
import requests

st.title("Intelligent Resume Screening Tool")

resume_input = st.text_area("Paste Resume Text")
job_desc_input = st.text_area("Paste Job Description")

if st.button("Evaluate Match"):
response = requests.post("http://localhost:5000/match", json={
"resume": resume_input,
"job_description": job_desc_input
})

    if response.ok:
        data = response.json()
        st.subheader(f"Match Score: {data['match_score']}%")
        st.text(data['summary'])
        st.write("**Skills Identified:**", ', '.join(data['skills']))
    else:
        st.error("Error from server")

# Folder: frontend/app.py

import streamlit as st
import requests

st.title("Intelligent Resume Screening Tool")

resume_input = st.text_area("Paste Resume Text")
job_desc_input = st.text_area("Paste Job Description")

if st.button("Evaluate Match"):
response = requests.post("http://localhost:5000/match", json={
"resume": resume_input,
"job_description": job_desc_input
})

    if response.ok:
        data = response.json()
        st.subheader(f"Match Score: {data['match_score']}%")
        st.text(data['summary'])
        st.write("**Skills Identified:**", ', '.join(data['skills']))
    else:
        st.error("Error from server")

This tool helps recruiters automatically screen and score resumes based on job descriptions.

## Features

- Resume parsing
- Match scoring with Sentence Transformers
- Web interface with Streamlit or API with Flask

## Setup

```bash
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

## Run

```bash
python backend/app.py
streamlit run frontend/app.py
```
