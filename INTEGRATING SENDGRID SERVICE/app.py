import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()


def send_email(to_email, subject, message):
    message = Mail(
        from_email='harshini.s.2019.cse@ritchennai.edu.in',
        to_emails='amritavarsheni.a.2019.cse@ritchennai.edu.in',
        subject='Sending with twilio sendgrid is fun',
        html_content=message)
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)