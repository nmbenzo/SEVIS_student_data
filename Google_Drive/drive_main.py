import shutil
import Google_Drive.manage_team_drives as team_drive
import Google_Drive.download_files as dl
import Google_Drive.Drive_API_Setup as setup
from Handlers.file_imports import location_a, location_b
import Handlers.Google_Drive_IDs as ids
import logging


logging.basicConfig(format='%(asctime)s %(levelname)-8s '
    '[%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt')

logger = logging.getLogger('Drive Logger')


def drive_sheet_upload():
    """Instantiates the Google Drive service and then uploads an xlsx file to
       the Team Drive of a specified ID"""
    try:
        driveInstance = team_drive.ManageTeamDrives(setup.DRIVE)
        upload_sheet_td = driveInstance.import_td_folder(name=ids.uploaded_file_name,
                        folder_id=ids.folder_id20, fn=ids.Registration_file,
                        mimeType=ids.SHEET_MIMETYPE)
        logger.info(f'{driveInstance, upload_sheet_td}')
        return upload_sheet_td
    except:
        print('An unknown error occurred, please check the logs.txt for more information.')


def drive_doc_upload():
    """Instantiates the Google Drive service and then uploads an .docx file to
       the Team Drive of a specified ID"""
    try:
        driveInstance = team_drive.ManageTeamDrives(setup.DRIVE)
        upload_doc_td = driveInstance.import_td_folder(name=ids.timeline_name,
                        folder_id=ids.folder_id20, fn=ids.REGISTRATION_TIMELINE,
                        mimeType=ids.DOC_MIMETYPE)
        logger.info(f'{driveInstance, upload_doc_td}')
        return upload_doc_td
    except:
        print('An unknown error occurred, please check the logs.txt for more information.')


def download_file():
    """Instantiates the Google Drive service and then runs the get_fileID
       method to get a file_id. download_file retrieves the file that matches
       the file_id returned from get_fileID"""
    try:
        driveInstance = dl.Download(setup.service)
        getID = driveInstance.get_fileID(ids.drive_file_name)
        file_download = driveInstance.download_file(mimeType=ids.Excel, file_name=ids.file_name, file_id=getID)
        shutil.move(location_a, location_b)
        logger.info(f'{driveInstance, getID, file_download}')
        return file_download
    except:
        print('An unknown error occurred, please check the logs.txt for more information.')


