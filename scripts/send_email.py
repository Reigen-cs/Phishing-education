import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email details
sender_email = "your_email@example.com"
receiver_email = "victim_email@example.com"
password = "your_password"

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Action Required: Update Your Account"

# Attach the HTML template
with open("email_template.html", "r") as file:
    html_content = file.read()
msg.attach(MIMEText(html_content, "html"))

# Send the email
try:
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
