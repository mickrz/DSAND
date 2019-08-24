"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

'''
Constants to reference the columns in the csv
'''
initiating_telephone_number = 0
receiving_telephone_number = 1
timestamp_of_call_or_text = 2
duration_of_telephone_call_in_seconds = 3

# create a dictionary
telephone_number_time_tracker = {}
most_chatty_telephone_number = None

'''
Logs the time for each phone number
'''
def add_telephone_number_to_time_tracker(telephone_number, time_tracked):
    global most_chatty_telephone_number
    
    if telephone_number not in telephone_number_time_tracker.keys():
        telephone_number_time_tracker[telephone_number] = time_tracked
    else:
        telephone_number_time_tracker[telephone_number] = telephone_number_time_tracker[telephone_number] + time_tracked

    if most_chatty_telephone_number == None or\
      int(telephone_number_time_tracker[telephone_number]) > int(telephone_number_time_tracker[most_chatty_telephone_number]):
        most_chatty_telephone_number = telephone_number
    
'''
Cycles through the input
'''
def find_most_chatty_telephone_number(csv):
    for row in csv:
        add_telephone_number_to_time_tracker(row[initiating_telephone_number], int(row[duration_of_telephone_call_in_seconds]))
        add_telephone_number_to_time_tracker(row[receiving_telephone_number], int(row[duration_of_telephone_call_in_seconds]))
    
    print(most_chatty_telephone_number + " spent the longest time, " +\
          str(telephone_number_time_tracker[most_chatty_telephone_number]) +\
          " seconds, on the phone during September 2016.")

find_most_chatty_telephone_number(calls)