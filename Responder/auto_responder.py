#This is an outline of the auto-responder, will be updated.
def send_response(email_id, response_type="warning"):
    if response_type == "warning":
        print(f"[AutoResponder] Warning: Email '{email_id}' flagged as phishing.")
    elif response_type == "auto_reply":
        print(f"[AutoResponder] Sent auto-reply to email '{email_id}'.")
    elif response_type == "report":
        print(f"[AutoResponder] Reported email '{email_id}' to security team.")
    else:
        print(f"[AutoResponder] Unknown response type for email '{email_id}'.")
