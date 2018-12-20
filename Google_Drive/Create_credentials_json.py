from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


# run this application to create a "credentials.json" file
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)