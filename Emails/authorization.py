from Google_Drive.Google_Drive_API_Handlers import *


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = NameError


class Auth:
    def __init__(self, SCOPES, client_secret, APPLICATION_NAME):
        self.SCOPES = SCOPES
        self.client_secret = client_secret
        self.APPLICATION_NAME = APPLICATION_NAME

    def get_credentials(self):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(self.client_secret, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            if flags:
                creds = tools.run_flow(flow, store, flags)
            else:
                creds = tools.run_flow(flow, store)

        return creds 
    