from Emails.Gmail_API_Handlers import *
from Emails.email_content import data_901, data_bad_phone, data_bad_addy, \
data_sv
from Emails.emails import isss, test_list, my_email


e_content_list = {
    'a': data_bad_addy,
    'p': data_bad_phone,
    's': data_sv,
    'f': data_901
}

e_group_list = {'is': isss, 'ts': test_list}

email_group_choices = ['is - ISSS Staff','ts - Test', 'sl - student list']

email_content_choices = [
    'a - Bad Address Email',
    'p - Bad Phone Email',
    's - Status Verification Incomplete Email',
    'f - I-901 Fee Unpaid',
    'Hit Enter to skip and create a custom message'
]


def get_emessage_content(e_content_list):
    print('\nWhich message would you like to send: ')
    for choice in email_content_choices:
        print(choice)
    content = input('\nYour Choice: ')
    for x in e_content_list.keys():
        if x == content:
            return e_content_list[x]


def get_eblast_list(e_group_list):
    print('\nPick a target group:')
    for choice in email_group_choices:
        print(choice)
    which_list = input('\nInput a group you like to blast message: ')
    for x in e_group_list.keys():
        if x == which_list:
            return e_group_list[x]


def singular_email(get_emessage_content):
    """
    Function takes in input from a user to specify the receiver and the email
    subject and then sends a message with a defined body of content
    """
    sendInstance = send_mail.SendEmail(service)
    receiver_input = input('Receiver Email: ')
    try:
        if get_emessage_content != None:
            subject_input = input('Email Subject: ')
            message = sendInstance.create_message(my_email,
            receiver_input, subject_input, get_emessage_content)
            sendInstance.send_message('me',message)
            print(f'\nEmail sent to {receiver_input}!')
        if get_emessage_content == None:
            subject_input = input('Email Subject: ')
            content = input('Please type your message: ')
            message = sendInstance.create_message(my_email,
            receiver_input, subject_input, content)
            sendInstance.send_message('me', message)
            print(f'\nEmail sent to {receiver_input}!')
    except:
        print('You must type a message body if one is not chosen '
              'from get_emessage_conetnt')




def multiple_emails(get_eblast_list, get_emessage_content):
    """
    Function takes in input from a user to specify the email
    subject and then sends a message with a defined body of content to several
    email addresses by looping through a list of emails [i].
    """
    sendInstance = send_mail.SendEmail(service)
    try:
        if get_emessage_content != None:
            subject_input = input('Email Subject: ')
            for email in get_eblast_list:
                message = sendInstance.create_message(my_email,
                email, subject_input, get_emessage_content)
                sendInstance.send_message('me', message)
                print(f'\nEmail sent to {email} in email list!')
        if get_emessage_content == None:
            subject_input = input('Email Subject: ')
            content = input('Please type your message: ')
            for email in get_eblast_list:
                message = sendInstance.create_message(my_email,
                email, subject_input, content)
                sendInstance.send_message('me', message)
                print(f'\nEmail sent to {email} in email list!')
    except:
        print('You must type a message body if one is not chosen '
              'from get_emessage_conetnt')