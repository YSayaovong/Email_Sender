import smtplib
from email.message import EmailMessage

# Create the email content
email = EmailMessage()
email['From'] = '<EMAIL>'
email['To'] = '<EMAIL>'
email['Subject'] = 'Hello World'
email.set_content('Hello World')

# Set up the server and login
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('<EMAIL>', 'password')

        # Send teh email
        smpt.send_message(email)
        print('Email was sent succesfully!')

except Exception as e:
    print(f"An error occurred: {e}")