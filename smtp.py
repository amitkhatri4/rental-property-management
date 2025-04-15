import smtplib
from email.mime.text import MIMEText

sender = "your_email@gmail.com"
receiver = "recipient@example.com"
password = "your_app_password"  # Use App Password if 2FA is on

msg = MIMEText("Hello from Python!")
msg["Subject"] = "Test Email"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)

print("Email sent successfully.")
