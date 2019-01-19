from Google_Drive.Google_Drive_API_Handlers import *


def drive_sheet_upload():
    """Instantiates the Google Drive service and then uploads an xlsx file to
       the Team Drive of a specified ID"""
    driveInstance = manage_team_drives.Manage_Team_Drives(DRIVE)
    upload_sheet_td = driveInstance.import_td_folder(name=uploaded_file_name, folder_id=folder_id, fn=Registration_file, mimeType=SHEET_MIMETYPE)

    return upload_sheet_td


def drive_doc_upload():
    """Instantiates the Google Drive service and then uploads an .docx file to
       the Team Drive of a specified ID"""
    driveInstance = manage_team_drives.Manage_Team_Drives(DRIVE)
    upload_doc_td = driveInstance.import_td_folder(name=timeline_name, folder_id=folder_id, fn=REGISTRATION_TIMELINE, mimeType=DOC_MIMETYPE)

    return upload_doc_td


def download_file():
    """Instantiates the Google Drive service and then runs the get_fileID
       method to get a file_id. download_file retrieves the file that matches
       the file_id returned from get_fileID"""
    driveInstance = download_files.Download(service)
    getID = driveInstance.get_fileID(uploaded_file_name)
    file_download = driveInstance.download_file(Excel, file_name, getID)

    return file_download

