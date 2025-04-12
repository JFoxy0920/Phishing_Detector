import re


def clean_email_text(text):
    #Remove whitespace and HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_urls(text):
    url_pattern = r'https?://\S+|www\.\S+'
    return re.findall(url_pattern, text)

def contains_suspicious_keywords(text, keywords):
    return any(keyword.lower() in text.lower() for keyword in keywords)
