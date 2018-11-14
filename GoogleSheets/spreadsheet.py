import gspread
from oauth2client.service_account import ServiceAccountCredentials
from XLSX_to_CSV.converter import newstudent_excel_to_csv
from New_Student_Registration.build_new_student_advisor_notes import ws2



def authenticate_google_docs():
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    gc = gspread.authorize(creds)
    return gc

gc = authenticate_google_docs()

sh = gc.open('201920 SEVIS Registration')
# print(sh.id)

worksheet_list = sh.worksheets()
# print(worksheet_list)

# Naming convention for this gs.workbook

# COL = sh.worksheet('COL')
# transferUG = sh.worksheet('Transfer UG')
# transferGR = sh.worksheet('Transfer GR')
# new_students = sh.worksheet('New Students')
# continuing_students = sh.worksheet('Continuing Students')


def update_new_students(sh):
    newstudent_excel_to_csv()
    content = open('new_student.csv', 'r').read()
    gc.import_csv(sh.id, content)

update_new_students(sh)

