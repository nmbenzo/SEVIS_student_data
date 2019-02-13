import shutil
import Google_Drive.manage_team_drives as team_drive
import Google_Drive.download_files as dl
import Google_Drive.Drive_API_Setup as setup
from Handlers.file_imports import location_a, location_b
from Handlers.Google_Drive_IDs import *


def drive_sheet_upload():
    """Instantiates the Google Drive service and then uploads an xlsx file to
       the Team Drive of a specified ID"""
    driveInstance = team_drive.ManageTeamDrives(setup.DRIVE)
    upload_sheet_td = driveInstance.import_td_folder(name=uploaded_file_name, folder_id=folder_id, fn=Registration_file, mimeType=SHEET_MIMETYPE)

    return upload_sheet_td


def drive_doc_upload():
    """Instantiates the Google Drive service and then uploads an .docx file to
       the Team Drive of a specified ID"""
    driveInstance = team_drive.ManageTeamDrives(setup.DRIVE)
    upload_doc_td = driveInstance.import_td_folder(name=timeline_name, folder_id=folder_id, fn=REGISTRATION_TIMELINE, mimeType=DOC_MIMETYPE)

    return upload_doc_td


def download_file():
    """Instantiates the Google Drive service and then runs the get_fileID
       method to get a file_id. download_file retrieves the file that matches
       the file_id returned from get_fileID"""
    driveInstance = dl.Download(setup.service)
    getID = driveInstance.get_fileID(drive_file_name)
    file_download = driveInstance.download_file(Excel, file_name, getID)
    shutil.move(location_a, location_b)

    return file_download
