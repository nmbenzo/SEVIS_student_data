from Emails.Gmail_API_Handlers import *
from Emails.email_content import data_901


def singular_email():
    """
    Function takes in input from a user to specify the receiver and the email
    subject and then sends a message with a defined body of content
    """
    sendInstance = send_mail.SendEmail(service)
    receiver_input = input('Receiver Email: ')
    subject_input = input('Email Subject: ')
    message = sendInstance.create_message('nbenzschawel@usfca.edu', receiver_input, subject_input, data_901)
    sendInstance.send_message('me',message)


def multiple_emails(emails):
    """
    Function takes in input from a user to specify the email
    subject and then sends a message with a defined body of content to several
    email addresses by looping through a list of emails [i].
    """
    sendInstance = send_mail.SendEmail(service)
    subject_input = input('Email Subject: ')
    for i in emails:
        message = sendInstance.create_message('nbenzschawel@usfca.edu', i, subject_input, data_901)
        sendInstance.send_message('me', message)