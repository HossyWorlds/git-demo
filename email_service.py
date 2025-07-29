def send_email(to, subject, body):
    # Feature D: Email notification service
    print(f"Sending email to: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    return {"status": "sent", "to": to, "subject": subject}

def send_notification(user, message):
    return send_email(
        to=f"{user}@example.com",
        subject="System Notification",
        body=message
    )