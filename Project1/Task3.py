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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

'''
Constants to reference the columns in the csv
'''
initiating_telephone_number = 0
receiving_telephone_number = 1
timestamp_of_call_or_text = 2
duration_of_telephone_call_in_seconds = 3

# PART A:

'''
Mobile numbers have no parentheses, but have a space in the middle
of the number to help readability. The prefix of a mobile number
is its first four digits, and they always start with 7, 8 or 9.
'''
def is_mobile_number(telephone_number):
    # normally I would have used regex to compile expression and find match
    if telephone_number[5] == ' ' and -1 == telephone_number.find("(")\
        and -1 == telephone_number.find(")") and telephone_number[0] == '7'\
        or telephone_number[0] == '8' or telephone_number[0] == '9':
            return telephone_number[0:4]
    return None

'''
Fixed lines start with an area code enclosed in brackets. The area
codes vary in length but always begin with 0.
'''
def is_fixed_line_number(telephone_number):
    # normally I would have used regex to compile expression and find match
    pos = telephone_number.find("(080)")
    if -1 != pos:
        return "080"
    return None

'''
Telemarketers' numbers have no parentheses or space, but they start
with the area code 140.
'''
def is_telemarketer_number(telephone_number):
    # normally I would have used regex to compile expression and find match
    pos = telephone_number.find("140")
    if -1 != pos and pos == 0:
        return "140"
    return None

'''
Cycle through the different types of telephone numbers to derive the
area code.
'''
def get_area_code(telephone_number):
    area_code = is_mobile_number(telephone_number)
    if area_code is None:
        area_code = is_fixed_line_number(telephone_number)
        if area_code is None:
            area_code = is_telemarketer_number(telephone_number)
    return area_code

'''
The generator will print each area code at a time before
processing the next telephone number
'''
def telephone_number_generator(csv):
    i = 0
    
    while True:
        row = csv[i]
        area_code = get_area_code(row[receiving_telephone_number])
        yield area_code
        i += 1

'''
The main method that runs the generator to get the desired output.
'''
def run_generator(csv):
    area_code_gen = telephone_number_generator(csv)
    total_iterations = len(csv)
    area_code_list = []
    
    print("The numbers called by people in Bangalore have codes:")
    for i in range(total_iterations):
        area_code = next(area_code_gen)
        if area_code not in area_code_list and area_code is not None:
            area_code_list.append(area_code)
    area_code_list.sort(key=lambda n: n.upper())
    
    for area_code in area_code_list:
        print(area_code)

run_generator(calls)

# PART B:
def calculate_fixed_line_to_fixed_line_call_percentage(csv):
    fixed_line_to_fixed_line_call = 0
    total_from_fixed_line = 0
    for row in csv:
        origination = is_fixed_line_number(row[initiating_telephone_number])
        destination = is_fixed_line_number(row[receiving_telephone_number])

        if origination is not None:
            total_from_fixed_line += 1
            if destination is not None:
                fixed_line_to_fixed_line_call += 1
                
    percentage = 100 * fixed_line_to_fixed_line_call / total_from_fixed_line
    print(str("%.2f" % percentage) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
    
calculate_fixed_line_to_fixed_line_call_percentage(calls)