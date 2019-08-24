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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

'''
Constants to reference the columns in the csv
'''
initiating_telephone_number = 0
receiving_telephone_number = 1
timestamp_of_call_or_text = 2
duration_of_telephone_call_in_seconds = 3

'''
Scans the list of numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls to present as a potential
telemarketer.
'''
def is_potential_telemarketers(call, texts):
    telemarketer_list = []
    for row in calls:
        if row[initiating_telephone_number] not in telemarketer_list:
            telemarketer_list.append(row[initiating_telephone_number])
            
    for row in calls:
        if row[receiving_telephone_number] in telemarketer_list:
            telemarketer_list.remove(row[receiving_telephone_number])
            
    for row in texts:
        if row[initiating_telephone_number] in telemarketer_list:
            telemarketer_list.remove(row[initiating_telephone_number])

        if row[receiving_telephone_number] in telemarketer_list:
            telemarketer_list.remove(row[receiving_telephone_number])
    
    print("These numbers could be telemarketers: ")
    telemarketer_list.sort(key=lambda n: n.upper())

    for telephone_number in telemarketer_list:
        print(telephone_number)

is_potential_telemarketers(calls, texts)