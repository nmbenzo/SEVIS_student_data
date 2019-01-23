from __future__ import print_function
import io
import uuid
from apiclient import discovery
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaIoBaseDownload
from Google_Drive import drive_authorization, manage_team_drives
from Google_Drive import download_files
from Handlers.Google_Drive_IDs import *


SCOPES = ['https://www.googleapis.com/auth/drive']
client_secret = 'client_secrets.json'
APPLICATION_NAME = 'Google Drive API'

# Building an instance of the Drive authorization class
drive_authInstance = drive_authorization.Auth(SCOPES, client_secret, APPLICATION_NAME)
# Building an instance of the credentials method
creds = drive_authInstance.get_credentials()

# Building the Drive and Service instance for usage in the Download and
# ManageTeamDrives classes
DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
service = build('drive', 'v3', http=creds.authorize(Http()))

# Returns a list of files, IDs, and Mimetypes in the Drive authorized with the
# credentials returned
files = DRIVE.files().list().execute().get('files', [])
