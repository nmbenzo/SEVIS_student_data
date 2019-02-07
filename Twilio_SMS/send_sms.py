from twilio.rest import Client
from Twilio_SMS.auth_token import account_sid, auth_token, myTwilionum
from Twilio_SMS.message_lists import *
from Twilio_SMS.sms_templates import *


client = Client(account_sid, auth_token)


def get_blast_list():
    which_list = input("Input a group you like to blast message: ")
    if which_list == 'isss_list':
        return isss_list
    if which_list == 'test_list':
        return test_list


def get_message_content():
    print('Which message would you like to send: \ns - Status Verification '
          'Incomplete \nt - Test \ng - General ISSS \nHit Enter to skip '
          'and create a custom message' )
    content = input('\nYour Choice: ')
    if content == 's':
        return SV_body
    if content == 't':
        return Test_response
    if content == 'g':
        return General_ISSS_response
    else:
        return None


def send_sms(client, *get_message_content):
    receiver = input('Phone Number: ')
    try:
        if get_message_content != None:
            message = client.messages. \
            create(body=get_message_content, from_=myTwilionum, to=receiver)
            print(message.sid)
            print(f'Message Sent to {receiver}')
    except:
        content = input('Please type your message: ')
        message = client.messages. \
            create(body=content, from_=myTwilionum, to=receiver)
        print(message.sid)
        print(f'Message Sent to {receiver}')


def send_blast_sms(client, get_blast_list, body):
    for number in get_blast_list:
        message = client.messages. \
            create(body=body, from_=myTwilionum, to=number)
        print(message.sid)
        print('Messages sent to users in requested list')
