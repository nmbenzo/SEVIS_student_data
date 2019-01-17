from __future__ import print_function
import httplib2
from apiclient import discovery
from oauth2client import tools
from Emails import authorization
from Emails import send_mail
from Emails.email_content import Header_901, file_901_fee, test_file


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


SCOPES = 'https://mail.google.com/'
client_secret = 'credentials.json'
APPLICATION_NAME = 'Gmail API Python Send Email'
authInstance = authorization.Auth(SCOPES, client_secret, APPLICATION_NAME)
credentials = authInstance.get_credentials()

http = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)


def get_labels():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])


sendInstance = send_mail.SendEmail(service)
message = sendInstance.create_message('your@gmail.com','receiver@gmail.com', 'Subject', 'Content')
sendInstance.send_message('me',message)
