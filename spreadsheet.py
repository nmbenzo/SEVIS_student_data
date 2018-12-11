import gspread
from oauth2client.service_account import ServiceAccountCredentials
from major_advisor_data import advisor_major_ug, advisor_major_gr


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Legislators 2017").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
list_of_values = sheet.get_all_values()

print(list_of_hashes)


sheet.update_cell(2,2, 'Benzschawel')

cell_list = sheet.range('A543:B546')
cell_values = ['Cynthia', 'MSDS', 'Nina', 'BENI', 'Marcella', 'APS', 'Nathan', 'CS']

for i, val in enumerate(cell_values):  # gives us a tuple of an index and value
    cell_list[i].value = val # use the index on cell_list and the val from cell_values

sheet.update_cells(cell_list)

cell_values = [
    {'Cynthia': 'MSDS'}
]


def _findadvisor(data, search_for):
    for k in data:
        for v in data[k]:
            if search_for in v:
                return k
    return None

print(_findadvisor(advisor_major_ug, 'BIO'))


def sheet_updates(_findadvisor):
    major_list = sheet.findall('MSDS')
    if _findadvisor == major_list:
        sheet.update_cell(_findadvisor) # need to specify which column to update


major_list = sheet.findall('MSDS')
print(major_list)


sheet_updates(_findadvisor(advisor_major_gr, 'MSDS'))

