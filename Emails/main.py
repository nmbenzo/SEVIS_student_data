from Handlers.Gmail_API_Handlers import *
from Emails.email_content import Header_901, file_901_fee


def mainEmail():
    sendInstance = send_mail.SendEmail(service)
    message = sendInstance.create_message('nbenzschawel@usfca.edu','nmbenzo@gmail.com', Header_901, file_901_fee)
    sendInstance.send_message('me',message)

