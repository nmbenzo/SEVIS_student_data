from twilio.rest import Client
from Twilio_SMS.auth_token import account_sid, auth_token, myTwilionum
from Twilio_SMS.message_lists import *
from Twilio_SMS.sms_templates import *


client = Client(account_sid, auth_token)

group_list = {'is': isss_list, 'ts': test_list, 'kb': k_b}

content_list = {'s': SV_body, 't': Test_response,
                'g': General_ISSS_response, 'gr': General_response}


def get_blast_list(group_list):
    print('\nPick a target group: \nis - ISSS Staff \nts - Test')
    which_list = input('\nInput a group you like to blast message: ')
    for x in group_list.keys():
        if x == which_list:
            return group_list[x]


def get_message_content(content_list):
    print('\nWhich message would you like to send: \ns - Status Verification '
          'Incomplete \nt - Test \ng - General ISSS \ngr - General ISSS Response '
          '\nHit Enter to skip and create a custom message' )
    content = input('\nYour Choice: ')
    for x in content_list.keys():
        if x == content:
            return content_list[x]


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
    if body != None:
        for number in get_blast_list:
            message = client.messages. \
            create(body=body, from_=myTwilionum, to=number)
            print(message.sid)
            print(f'Message Sent to {number}')
    if body == None:
        content = input('Please type your message: ')
        for number in get_blast_list:
            message = client.messages. \
                create(body=content, from_=myTwilionum, to=number)
            print(message.sid)

    print('Messages sent to users in requested list')

