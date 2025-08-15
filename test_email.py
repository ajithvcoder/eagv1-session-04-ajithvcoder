import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()

app_password = os.getenv("G_APP_PASS")

# Gmail account details
sender_email = "inocajith21.5@gmail.com"
receiver_email = "inocajith21.5@gmail.com"

# Create email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email from Python"

# Body of the email
body = "Hello, this is a test email sent from Python! by ajithvcoder"
msg.attach(MIMEText(body, "plain"))

# Send email via Gmail's SMTP server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, app_password)
    server.send_message(msg)

print("Email sent successfully!")
