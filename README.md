# SEVIS_Student_data
A variety of files to connect Excel spreadsheet data of students for SEVIS reporting compliance. 

These files allow international student advisors to build data on students via the openpyxl and pandas modules in Python.

Several of these modules may require modifications based on your own reports (column values, report names and directories).

The purpose of this project was to automate populating certain data required by advisors for tracking students. Data reporting
from ISSM did not meet the needs of our office, so I built this application to improve data management efficiency.

Originally, my process was to copy and paste data from various profiles into a spreadsheet and then merge these spreadsheets into one Workbook and upload to a Google TeamDrive. This is now automated in Python.

This module was built with PyCharm CE and has several libraries installed on the main Python 3.7 directory: usr/local/bin/python3.7 

The following modules will need to be installed in your Python directory or (virtual environment):
* openpyxl 2.5.6 or newer
* gspread 3.1.0 or newer
* pandas 0.23.4 or newer
* googleapis module 

Due to FERPA regulations, I cannot include the actual .xlsx files as they contain sensitive student data, however, please feel free to reach out to me if you'd like to set up a similar process for automating data population in Excel with Python.
nmbenzo@gmail.com

For more information on how to setup and configure the gspread module, please see the following link: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

---Recent Additions---

***Added basic Twilio SMS integration

***Added Gmail emailing capabilities

***Added Google TeamDrive syncing: uploading and downloading

***Expanded menu options 


---Short-Term Future Development---

***Add SMTP Email capability for MS Outlook

***Create "Search for" module to search for files. This will improve scalability

***Add logging 

***Add threading and async to improve performance


---Long-Term Future Development---

***Pull data directly from ISSM and SEVIS

***Build web app GUI


