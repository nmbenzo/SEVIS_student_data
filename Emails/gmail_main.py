from Emails.Gmail_API_Handlers import *
from Emails.email_content import Header_901, test_file


def mainEmail():
    sendInstance = send_mail.SendEmail(service)
    message = sendInstance.create_message('nbenzschawel@usfca.edu','nbenzschawel@usfca.edu', 'Final Python Application', test_file)
    sendInstance.send_message('me',message)
