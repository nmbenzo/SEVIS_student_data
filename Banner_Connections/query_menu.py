from Banner_Connections.queries import *


query_list = \
    ['s - Query single CWID and extract a phone number for SMS',
    'e - Query single CWID and extract a phone number for email',
    'bs - Query several test CWIDs for messaging']

query_choices = {
    's': run_single_email_query(),
    'e': run_single_email_query(),
    'bs': blast_cell_test
}


def choose_query(query_choices):
    print('Please select the query you\'d like to run: ')
    for choice in query_list:
        print(choice)
    content = input('\nYour Choice: ')
    for x in query_choices.keys():
        if x == content:
            return query_choices[x]