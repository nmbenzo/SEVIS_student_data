from __future__ import print_function
import io
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaIoBaseDownload


# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

# The ID and range of a sample spreadsheet.
file_id = '1MGAT36t17ZluulYx698lPA26lmfqcHQNFUoF_cM_O9w'
Excel = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
file_name = 'SEVIS Registration'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=50, supportsTeamDrives=True, includeTeamDriveItems=True,
        corpora='teamDrive', teamDriveId='0ADUIPThXplYvUk9PVA',
        fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))


    data = service.files().export(fileId=file_id, mimeType=Excel).execute()
    meta = service.files().get(fileId=file_id, fields="*",
                                    supportsTeamDrives=True).execute()

    print(meta)



main()