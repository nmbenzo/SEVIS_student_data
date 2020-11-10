import time
import io
from googleapiclient.http import MediaIoBaseDownload
from Handlers.Google_Drive_IDs import td_id, Excel, drive_file_name
from tqdm import trange


class Download:
    """A simple class to retrieve passed file names, types, and ids
    to download a file from google drive"""
    def __init__(self, service):
        """Initializes the service parameter"""
        self.service = service

    def get_fileID(self, file_name):
        """
        Call the Drive v3 API to get the file_id for a particular file name
        which is passed as an argument
        """
        results = self.service.files().list(
            pageSize=50,
            supportsTeamDrives=True,
            includeTeamDriveItems=True,
            corpora='teamDrive',
            teamDriveId=td_id,
            fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        for i in items:
            if i['name'] == file_name:
                return i['id']

    def download_file(self, mimeType, file_name, file_id):
        """
        Call the Drive v3 API and then download a file if the file ID matches a
        specified name matches the name passed to the get_file_ID method.
        """
        drive_files = self.service.files().list(
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

        data = self.service.files().export_media(fileId=file_id, mimeType=Excel)
        fh = io.FileIO(file_name, 'wb')
        downloader = MediaIoBaseDownload(fh, data)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        for i in trange(100):
            time.sleep(0.01)

        for f in drive_files['files']:
            if f['id'] == self.get_fileID(drive_file_name):
                print('Downloaded: ' + f['name'])

