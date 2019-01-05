import os
os.getcwd()
from Handlers.file_imports import ws1


SEVISID_completed = []

for row in range(2, ws1.max_row):
    id = ws1.cell(row=row, column=1).value
    SEVISID_completed.append(id)




