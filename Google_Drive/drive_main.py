from Google_Drive.Google_Drive_API_Handlers import *


def drive_sheet_upload():
    driveInstance = manage_team_drives.Manage_Team_Drives(DRIVE)
    upload_sheet_td = driveInstance.import_td_folder(name=uploaded_file_name, folder_id=folder_id, fn=Registration_file, mimeType=SHEET_MIMETYPE)

    return upload_sheet_td


def drive_doc_upload():
    driveInstance = manage_team_drives.Manage_Team_Drives(DRIVE)
    upload_doc_td = driveInstance.import_td_folder(name=timeline_name, folder_id=folder_id, fn=REGISTRATION_TIMELINE, mimeType=DOC_MIMETYPE)

    return upload_doc_td


