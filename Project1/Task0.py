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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

'''
Constants to reference the columns in the csv
'''
initiating_telephone_number = 0
receiving_telephone_number = 1
timestamp_of_call_or_text = 2
duration_of_telephone_call_in_seconds = 3

first_row = texts[0] 
print("First record of texts, " + first_row[initiating_telephone_number] +\
      " texts " +  first_row[receiving_telephone_number] + " at time " +\
      first_row[timestamp_of_call_or_text])

last_row = calls[(len(calls) - 1)] 
print("Last record of calls, " + last_row[initiating_telephone_number] +\
      " calls " + last_row[receiving_telephone_number] + " at time " +\
      last_row[timestamp_of_call_or_text] + ", lasting " +\
      last_row[duration_of_telephone_call_in_seconds] + " seconds")