# 🧠 Intelligent Resume Screening Tool (AI Recruiter Assistant)

This AI-powered tool helps recruiters screen and rank resumes against job descriptions using NLP and machine learning.

---

## 🚀 Features

- 📝 **Resume Parser**: Extracts summary and skills from plain text resumes using spaCy.
- 🔍 **Job Matching**: Uses Sentence Transformers to compute similarity between resumes and job descriptions.
- 📊 **Match Score & Fit Summary**: See how well a resume aligns with a job posting.
- 🌐 **User Interface**: Simple Streamlit web app for interactive use.

---

## 🧰 Tech Stack

| Layer       | Technology                                        |
| ----------- | ------------------------------------------------- |
| Frontend    | Streamlit                                         |
| Backend     | Flask (REST API)                                  |
| ML/NLP      | spaCy, Sentence Transformers, NLTK                |
| PDF Support | pdfminer.six                                      |
| Testing     | Pytest                                            |
| Deployment  | [Render.com](https://render.com), Streamlit Cloud |

---

## 📂 Folder Structure

resume_screening_tool/
│
├── backend/ # Flask API + NLP logic
│ ├── app.py
│ ├── resume_parser.py
│ ├── job_matcher.py
│ └── requirements.txt
│
├── frontend/ # Streamlit UI
│ ├── app.py
│ └── requirements.txt
│
├── test/ # Unit tests
│ ├── test_resume_parser.py
│ └── test_job_parser.py
│
├── data/ # Sample files
│ ├── sample_resume.txt
│ └── sample_job_desc.txt
│
├── docs/ # Project documentation
│ └── README.md
│
├── .gitignore
├── LICENSE
└── README.md # This file

## ⚙️ Setup Instructions

### 📌 1. Clone & Set Up Virtual Environment

git clone https://github.com/your-username/resume_screening_tool.git
cd resume_screening_tool
python -m venv venv310
source venv310/bin/activate # On Windows: venv310\Scripts\activate
📌 2. Install Dependencies

pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
python -m spacy download en_core_web_sm
🚦 Run the App
▶️ Start Flask API

python backend/app.py
▶️ Start Streamlit Frontend (in a new terminal)

streamlit run frontend/app.py
🧪 Run Tests

📷 Demo Screenshot

🛠️ Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

📄 License
This project is licensed under the MIT License.

👨‍💻 Author
Developed by Umar | [Your GitHub or LinkedIn link]

Would you like me to generate the `demo_screenshot.png` image or help you deploy it to Streamlit Cloud or Render.com next?
