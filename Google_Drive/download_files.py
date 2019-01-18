from Google_Drive.Google_Drive_API_Handlers import *
from Handlers.Google_Drive_IDs import td_id, SCOPES, \
    Excel, uploaded_file_name



def get_fileID(uploaded_file_name):
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=50,
        supportsTeamDrives=True,
        includeTeamDriveItems=True,
        corpora='teamDrive',
        teamDriveId=td_id,
        fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    for i in items:
        if i['name'] == uploaded_file_name:
            return i['id']


def download_file(mimeType, file_name, file_id = get_fileID(uploaded_file_name)):
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
    drive_files = service.files().list(
        pageSize=50,
        supportsTeamDrives=True,
        includeTeamDriveItems=True,
        corpora='teamDrive',
        teamDriveId=td_id,
        fields="nextPageToken, files(id, name)").execute()
    items = drive_files.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')

    if 'google-apps' in mimeType:
        return

    data = service.files().export_media(fileId=file_id, mimeType=Excel)
    fh = io.FileIO(file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, data)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download: {}".format(int(status.progress() * 100)))

    for f in drive_files['files']:
        if f['id'] == get_fileID(uploaded_file_name):
            print('Downloaded: ' + f['name'])

