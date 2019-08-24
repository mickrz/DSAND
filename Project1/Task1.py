"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

'''
Constants to reference the columns in the csv
'''
initiating_telephone_number = 0
receiving_telephone_number = 1
timestamp_of_call_or_text = 2
duration_of_telephone_call_in_seconds = 3

unique_telephone_numbers = []
'''
Adds telephone number to list if unique
'''
def add_telephone_number_to_list(telephone_number):
    if telephone_number not in unique_telephone_numbers:
        unique_telephone_numbers.append(telephone_number)
        
'''
Takes the list and passes telephone numbers which are contained
in the first two columns
'''
def parse_telephone_data(input):
    for row in input:
        add_telephone_number_to_list(row[initiating_telephone_number])
        add_telephone_number_to_list(row[receiving_telephone_number])

'''
Main method that takes list of lists from csv and parses it
'''
def count_unique_telephone_numbers(texts, calls):
    parse_telephone_data(texts)
    parse_telephone_data(calls)
    print("There are " + str(len(unique_telephone_numbers)) + " different telephone numbers in the records.")
    
count_unique_telephone_numbers(texts, calls)