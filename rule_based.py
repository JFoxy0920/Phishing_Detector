def predict(subject, body):
    phishing_keywords = [
        "verify", "click here", "update your account", "login now",
        "urgent", "suspend", "compromised"
    ]
    text = (subject + ' ' + body).lower()
    for keyword in phishing_keywords:
        if keyword in text:
            return "phishing"
    return "legit"
