from __future__ import print_function
import io
import uuid
from apiclient import discovery
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaIoBaseDownload
from Google_Drive import drive_authorization, manage_team_drives
from Handlers.Google_Drive_IDs import *


SCOPES = ['https://www.googleapis.com/auth/drive']
client_secret = 'client_secrets.json'
APPLICATION_NAME = 'Google Drive API'

drive_authInstance = drive_authorization.Auth(SCOPES, client_secret, APPLICATION_NAME)
creds = drive_authInstance.get_credentials()

DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

files = DRIVE.files().list().execute().get('files', [])
