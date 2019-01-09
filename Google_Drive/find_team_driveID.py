from __future__ import print_function
import uuid
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools


scope = ['https://www.googleapis.com/auth/drive']
store = file.Storage('credentials.json')
creds = store.get()

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secrets_service_acc.json', scope)
    creds = tools.run_flow(flow, store)

DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))


team_drive_metadata = {'name': 'ISSS SEVIS and Immigration'}
request_id = str(uuid.uuid4())
team_drive = DRIVE.teamdrives().create(body=team_drive_metadata,
                                               requestId=request_id,
                                               fields='id').execute()
print('Team Drive ID: %s' % team_drive.get('id'))

