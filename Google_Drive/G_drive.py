from __future__ import print_function
import uuid
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools


"""This file provides oAuth credential access to Google Drive and Team Drives"""

# Define Level of Access (Scope) and Authorize credentials
scope = ['https://www.googleapis.com/auth/drive']
store = file.Storage('credentials.json')
creds = store.get()

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secrets.json', scope)
    creds = tools.run_flow(flow, store)

DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
files = DRIVE.files().list().execute().get('files', [])


def create_td(td_name):
    """Creates a new Team Drive"""
    request_id = str(uuid.uuid4()) # random unique UUID string
    body = {'name': td_name}
    return DRIVE.teamdrives().create(body=body,
            requestId=request_id, fields='id').execute().get('id')

def add_user(td_id, user, role='commenter'):
    """Adds specified users to a Team Drive"""
    body = {'type': 'user', 'role': role, 'emailAddress': user}
    return DRIVE.permissions().create(body=body, fileId=td_id,
            supportsTeamDrives=True, fields='id').execute().get('id')

def create_td_folder(td_id, folder):
    """Creates a folder within a Team Drive"""
    body = {'name': folder, 'mimeType': FOLDER_MIME, 'parents': [td_id]}
    return DRIVE.files().create(body=body,
            supportsTeamDrives=True, fields='id').execute().get('id')

def import_td_folder(folder_id, fn, mimeType):
    """Adds a specified file to the Team Drive
    and then converts it to a G-Suite format"""
    body = {'name': fn, 'mimeType': mimeType, 'parents': [folder_id]}
    return DRIVE.files().create(body=body, media_body=fn,
            supportsTeamDrives=True, fields='id').execute().get('id')


# Specifies the desired upload location and mimeType
FOLDER_MIME = 'application/vnd.google-apps.folder'
SOURCE_FILE = '/Users/nbenzschawel/Desktop/SEVIS_transfer_data.xlsx' # Example
MIMETYPE = 'application/vnd.google-apps.spreadsheet' # Example

td_id = 'XXXX' # unique ID from the Team Drive URL
folder_id = 'XXXX' # unique ID from the folder URL
file_id = import_td_folder(folder_id, SOURCE_FILE, MIMETYPE)
print(f'** {SOURCE_FILE} file imported as {MIMETYPE} in Team Drives folder **')

