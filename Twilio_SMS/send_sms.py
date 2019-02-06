from twilio.rest import Client
from Twilio_SMS.auth_token import account_sid, auth_token, myTwilionum


client = Client(account_sid, auth_token)


receiver = input('Phone Number: ')

message = client.messages. \
create(body="This is a test text message from Nathan's SEVIS App",
       from_=myTwilionum, to=receiver)


print(message.sid)