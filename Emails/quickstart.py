from __future__ import print_function
import httplib2
from apiclient import discovery
from oauth2client import file, client, tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


SCOPES = [
	'https://mail.google.com/', 'https://www.googleapis.com/auth/gmail.compose'
]
APPLICATION_NAME = 'Gmail API Python Send Email'


def get_credentials():
    """Shows basic usage of getting authorization credentials via the Gmail API

	The file token.json stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the first time.
	"""
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            creds = tools.run_flow(flow, store, flags)
        else:
            creds = tools.run_flow(flow, store)

    return creds


def main():
    """Shows basic usage of the Gmail API.
    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
      print('Labels:')
      for label in labels:
        print(label['name'])


if __name__ == '__main__':
    main()