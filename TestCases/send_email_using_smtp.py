from smtplib import SMTP_SSL, SMTP_SSL_PORT

SMTP_HOST = 'mail.example.com'
SMTP_USER = 'kh928259@gmail.com'
SMTP_PASS = 'Secret!'

# Craft the email by hand
from_email = 'My name <someone@example.com>'
to_emails = ['khanhhm.94@gmail.com', 'minhkhanh.huynh@shopee.com']
body = "Hello, world!"
headers = f"From: {from_email}\r\n"
headers += f"To: {', '.join(to_emails)}\r\n"
headers += f"Subject: Hello\r\n"
email_message = headers + "\r\n" + body  # Blank line needed between headers and body

# Connect, authenticate, and send mail
smtp_server = SMTP_SSL(SMTP_HOST, port=SMTP_SSL_PORT)
smtp_server.set_debuglevel(1)  # Show SMTP server interactions
smtp_server.login(SMTP_USER, SMTP_PASS)
smtp_server.sendmail(from_email, to_emails, email_message)

# Disconnect
smtp_server.quit()