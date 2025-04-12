# Phishing Email Detector

A Python-based tool that detects phishing emails using both rule-based and machine learning (ML) methods. Designed for cybersecurity projects and hands-on learning, this project supports batch email classification, detailed logging, and misclassification analysis.

---

## Features
- Rule-Based Detection (keywords and patterns)
- Machine Learning Detection (TF-IDF + Naive Bayes)
- Combined Prediction Logic
- Batch Classification with Output Logging
- Misclassification Reports
- Text-Based Summary of Misclassification Types

---

## Project Structure

phishing_email_detector/ <br/>
├── main.py # Main script to run classification <br/>
├── detector/ # Rule-based and ML detection modules<br/>
├── responder/ # Auto-responder logic (funcitonality to be improved)<br/>
├── utils/ # Email parsing utilities <br/>
├── data/ <br/>
└── sample_emails.csv # Sample labeled email dataset <br/>
├── requirements.txt <br/>
└── README.md<br/>

## Quick Start

### 1. Clone the Repo

git clone https://github.com/JFoxy0920/Phishing_Detector.git
cd phishing-email-detector

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the Tool
python main.py <br/>
Output:

classified_emails.csv — all emails with predicted labels

classified_emails_misclassified.csv — only misclassified emails

classified_emails_event_summary.txt — summary of common misclassification types

# Example Email Format:
subject,body,label <br/>
"Update Your Account","Dear user, click here to verify.",phishing <br/>
"Meeting Agenda","Here's the agenda for our meeting.",legit<br/>
Model Details <br/>
ML Model: Naive Bayes classifier <br/>

Vectorizer: TF-IDF on combined subject + body <br/>

Fallback: If ML and rule-based disagree, rule-based takes precedence for phishing

# Future Improvements
Auto-Responder Functionality

Integrate email fetching via IMAP

Train on larger datasets (e.g., Enron, PhishTank)

Add GUI with Flask or Streamlit

Advanced NLP explanations (e.g., highlighting risky words)
