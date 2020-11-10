import sys, os
import cx_Oracle
import traceback
import Banner_Connections.ODSP_Creds as creds
import pandas as pd
import Banner_Connections.queries as query
from tabulate import tabulate
from Handlers.directories import downloads_path


def banner_ods_handler():
  """Function to initialize an object from the cx_Oracle Connection class
  :returns a cx_Oracle Connection object if valid credentials exist otherwise
  prints a traceback error"""
  host = creds.host
  port = creds.port
  sid = creds.sid
  username = creds.username
  password = creds.password

  try:
    dsn = cx_Oracle.makedsn(host, port, sid)
    connection = cx_Oracle.Connection("%s/%s@%s" % (username, password, dsn))
    return connection
  except cx_Oracle.DatabaseError as exc:
    error, = exc.args
    print(sys.stderr, "Oracle-Error-Code:", error.code)
    print(sys.stderr, "Oracle-Error-Message:", error.message)
    tb = traceback.format_exc()
    return tb


def banner_ODSP_tele(connection, query_name):
  """The banner_ODSP_tele function takes in an connection
  argument to connect to ODSP. It then accepts a specific query
  as the second argument and returns the query results"""
  cursor = connection.cursor()
  cursor.execute(query_name)
  try:
    query_result = [(area_code, number) for area_code, number in cursor]
    cleaned_number = [''.join(number) for number in query_result]
    return cleaned_number
  finally:
    cursor.close()
    connection.close()


def banner_ODSP_tele_maj(connection, query_name):
  """The banner_ODSP_tele function takes in an connection
  argument to connect to ODSP. It then accepts a specific query
  as the second argument and returns the query results"""
  cursor = connection.cursor()
  cursor.execute(query_name)
  try:
    # banner area codes and phone numbers are stored as separate
    # attributes so they need to be joined as a string
    query_result = [(area_code, number) for area_code, number in cursor]
    cleaned_number = [''.join(number) for number in query_result]
    removed_duplicates = list(set(cleaned_number))
    return removed_duplicates
  finally:
    cursor.close()
    connection.close()


def banner_ODSP_emails(connection, query_name):
  """The banner_ODSP_tele function takes in an connection
  argument to connect to ODSP. It then accepts a specific email query
  as the second argument and returns the query results"""
  cursor = connection.cursor()
  cursor.execute(query_name)
  try:
    query_result = [email[0] for email in cursor]
    cleaned_email = ''.join(email for email in query_result)
    return cleaned_email
  finally:
    cursor.close()
    connection.close()


def banner_ODSP_graduated_students(connection, query_name):
  """The banner_ODSP_graduated_students function takes in an connection
  argument to connect to ODSP. It then accepts a specific query
  as the second argument and returns the query results"""
  cursor = connection.cursor()
  cursor.execute(query_name)
  try:
    query_result = [row for row in cursor]
    return query_result
  finally:
    cursor.close()
    connection.close()


def query_results_xlsx(sheet_name):
  """The genery_query_results function reads an ODSP query to a Dataframe
  and takes in an argument as a string for the sheet name. It then exports the
  query to an Excel file in the users Downloads directory"""
  df_query = pd.read_sql_query(query.choose_query(), banner_ods_handler())

  try:
    writer = pd.ExcelWriter(downloads_path + sheet_name + '.xlsx')
    df_query.to_excel(writer, 'Sheet1', index=False)
    writer.save()
    print('File: ' + sheet_name +'.xlsx exported to User/Downloads!')
  except Exception as e:
    print('The following error occurred: ' + str(e))


def print_query_results():
  """The print_query_results function takes in an connection
  argument to connect to ODSP. It then accepts a specific query
  specified by the user as an argument and prints the query results
  in a clean format using the tabulate library."""
  df_query = pd.read_sql_query(query.choose_query(), banner_ods_handler())
  print(tabulate(df_query, headers='keys', tablefmt='psql'))


def read_query_to_df():
  """Function reads a user selected query to a Pandas DataFrame
  :returns - DataFrame Object"""
  df_query = pd.read_sql_query(query.choose_query(), banner_ods_handler())
  return df_query

