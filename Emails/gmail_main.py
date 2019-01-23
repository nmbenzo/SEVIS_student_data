from Emails.Gmail_API_Handlers import *
from Emails.email_content import data_901


def singular_email():
    sendInstance = send_mail.SendEmail(service)
    receiver_input = input('Receiver Email: ')
    subject_input = input('Email Subject: ')
    message = sendInstance.create_message('nbenzschawel@usfca.edu', receiver_input, subject_input, data_901)
    sendInstance.send_message('me',message)


def multiple_emails(emails):
    sendInstance = send_mail.SendEmail(service)
    subject_input = input('Email Subject: ')
    for i in emails:
        message = sendInstance.create_message('nbenzschawel@usfca.edu', i, subject_input, data_901)
        sendInstance.send_message('me', message)