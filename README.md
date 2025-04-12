# 🛡Phishing Email Detector

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

phishing_email_detector/ 
├── main.py # Main script to run classification
├── detector/ # Rule-based and ML detection modules
├── responder/ # Auto-responder logic (optional)
├── utils/ # Email parsing utilities 
├── data/ 
│ └── sample_emails.csv # Sample labeled email dataset 
├── requirements.txt 
└── README.md

## Quick Start

### 1. Clone the Repo

git clone https://github.com/yourusername/phishing-email-detector.git
cd phishing-email-detector

### 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

### 3. Run the Tool
bash
Copy
Edit
python main.py
Output:

classified_emails.csv — all emails with predicted labels

classified_emails_misclassified.csv — only misclassified emails

classified_emails_event_summary.txt — summary of common misclassification types

# Example Email Format:
csv
Copy
Edit
subject,body,label
"Update Your Account","Dear user, click here to verify.",phishing
"Meeting Agenda","Here's the agenda for our meeting.",legit
Model Details
ML Model: Naive Bayes classifier

Vectorizer: TF-IDF on combined subject + body

Fallback: If ML and rule-based disagree, rule-based takes precedence for phishing

# Future Improvements
Integrate email fetching via IMAP

Train on larger datasets (e.g., Enron, PhishTank)

Add GUI with Flask or Streamlit

Advanced NLP explanations (e.g., highlighting risky words)
