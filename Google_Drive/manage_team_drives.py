from Handlers.Google_Drive_API_Handlers import *


"""This file provides oAuth credential access to Google Drive and Team Drives"""

class Manage_Team_Drives:

    def __init__(self, DRIVE):
        self.DRIVE = DRIVE

    def create_td(self, td_name):
        """Creates a new Team Drive"""
        request_id = str(uuid.uuid4()) # random unique UUID string
        body = {'name': td_name}
        return self.DRIVE.teamdrives().create(body=body,
                requestId=request_id, fields='id').execute().get('id')

    def add_user(self, td_id, user, role='commenter'):
        """Adds specified users to a Team Drive"""
        body = {'type': 'user', 'role': role, 'emailAddress': user}
        return self.DRIVE.permissions().create(body=body, fileId=td_id,
                supportsTeamDrives=True, fields='id').execute().get('id')

    def create_td_folder(self, td_id, folder):
        """Creates a folder within a Team Drive"""
        body = {'name': folder, 'mimeType': FOLDER_MIME, 'parents': [td_id]}
        return self.DRIVE.files().create(body=body,
                supportsTeamDrives=True, fields='id').execute().get('id')

    def import_td_folder(self, name, folder_id, fn, mimeType):
        """Adds a specified file to the Team Drive
        and then converts it to a G-Suite format"""
        body = {'name': name, 'originalFilename': fn, 'mimeType': mimeType, 'parents': [folder_id]}
        return self.DRIVE.files().create(body=body, media_body=fn,
                supportsTeamDrives=True, fields='id').execute().get('id')


"""
Example function call:

Sheet_file_id = import_td_folder(folder_id, SOURCE_FILE, SHEET_MIMETYPE)
Doc_file_id = import_td_folder(folder_id, SOURCE_FILE, DOC_MIMETYPE)
"""


