
### Task 0:
The run-time analysis is O(1) because it's just two constant-time statements where it is just getting an item from a list. It would take the same amount of time to run regardless of the size of the input. As for reading in the files, it is O(n) to read each csv file. I did not include this in the analysis for any of the tasks.

```python
first_row = texts[0]
last_row = calls[(len(calls) - 1)]
```

### Task 1:
The run-time is O(n x m) where n is the length of the input `csv` and m is the length of the `unique_telephone_list`. The main work for the run-time analysis is done in `parse_telephone_data(csv)` and `add_telephone_number_to_list`. There are technically two for loops executed, but the constant would be dropped as well as any additional constants for the code in the other methods (`count_unique_telephone_numbers` and `add_telephone_number_to_list`).

```python
def parse_telephone_data(csv):
    for row in csv:                                           <--- O(n)
        add_telephone_number_to_list(row[initiating_telephone_number])
        add_telephone_number_to_list(row[receiving_telephone_number])

def add_telephone_number_to_list(telephone_number):
    if telephone_number not in unique_telephone_numbers:      <--- O(m)
        unique_telephone_numbers.append(telephone_number)     <--- O(1)

def count_unique_telephone_numbers(texts, calls):
    parse_telephone_data(texts)                               <--- O(1)
    parse_telephone_data(calls)                               <--- O(1)
    print("There are " + str(len(unique_telephone_numbers)) + " different telephone numbers in the records.")
```

### Task 2:
Using a python dictionary turns out to be expensive since each time `add_telephone_number_to_time_tracker` is called incurs O(n). It is called twice per row in `find_most_chatty_telephone_number` which is already an O(m). Excluding constants, the worst-case is O(m x 2n) or just O(m x n).

```python
def add_telephone_number_to_time_tracker(telephone_number, time_tracked):
    global most_chatty_telephone_number
    
    if telephone_number not in telephone_number_time_tracker.keys():              <-- O(n)
        telephone_number_time_tracker[telephone_number] = time_tracked            <-- O(1) not found or found (if/else)
    else:
        telephone_number_time_tracker[telephone_number] = telephone_number_time_tracker[telephone_number] + time_tracked

    if most_chatty_telephone_number == None or\                                   <-- O(1)
      int(telephone_number_time_tracker[telephone_number]) > int(telephone_number_time_tracker[most_chatty_telephone_number]):
        most_chatty_telephone_number = telephone_number
    
def find_most_chatty_telephone_number(csv):
    for row in csv:                                                               <-- O(m)
        add_telephone_number_to_time_tracker(row[initiating_telephone_number], int(row[duration_of_telephone_call_in_seconds]))
        add_telephone_number_to_time_tracker(row[receiving_telephone_number], int(row[duration_of_telephone_call_in_seconds]))
    
    print(most_chatty_telephone_number + " spent the longest time, " +\
          str(telephone_number_time_tracker[most_chatty_telephone_number]) +\
          " seconds, on the phone during September 2016.")
```

### Task 3:

#### Part A:
The time complexity in `is_mobile_number()` is O(n x n) and `is_fixed_line_number` is O(m) and `is_telemarketer_number` is O(m). `run_generator` is O(a + blogb + b). Total time complexity is O(a) where a is reading the `csv`. The other terms do not dominate.

```python
def is_mobile_number(telephone_number):
    if telephone_number[5] == ' '
        and "(" not in telephone_number                                                             <-- O(n)
        and ")" not in telephone_number                                                             <-- O(n)
        and telephone_number[0] == '7' or telephone_number[0] == '8' or telephone_number[0] == '9': <-- O(1)
            return telephone_number[0:4]
    return None

def is_fixed_line_number(telephone_number):
    pos = telephone_number.find("080")                                                              <-- O(m)
    if -1 != pos:                                                                                   <-- O(1)
        return "080"
    return None

def is_telemarketer_number(telephone_number):
    pos = telephone_number.find("140")                                                              <-- O(m)
    if -1 != pos and pos == 0:                                                                      <-- O(1)
        return "140"
    return None

def get_area_code(telephone_number):
    area_code = is_mobile_number(telephone_number)                                                  <-- O(1)
    if area_code is None:                                                                           <-- O(1)
        area_code = is_fixed_line_number(telephone_number)                                          <-- O(1)
        if area_code is None:                                                                       <-- O(1)
            area_code = is_telemarketer_number(telephone_number)                                    <-- O(1)
    return area_code
        
def telephone_number_generator(csv):
    i = 0
    
    while True:
        row = csv[i]                                                                                <-- O(1)
        area_code = get_area_code(row[receiving_telephone_number])                                  <-- O(1)
        yield area_code                                                                             <-- O(1)
        i += 1                                                                                      <-- O(1)
        
def run_generator(csv):
    area_code_gen = telephone_number_generator(csv)
    total_iterations = len(csv)
    area_code_list = []
    
    print("The numbers called by people in Bangalore have codes:")
    for i in range(total_iterations):                                                               <-- O(a)
        area_code = next(area_code_gen)                                                             <-- O(1)
        if area_code not in area_code_list and area_code is not None:                               <-- O(1)
            area_code_list.append(area_code)                                                        <-- O(1)

    area_code_list.sort(key=lambda n: n.upper())                                                    <-- O(blogb)
    
    for area_code in area_code_list:                                                                <-- O(b)
        print(area_code)
```

#### Part B:
The time complexity is O(n x m). `n` represents reading all lines in `csv` and `m` represents checking if the telephone number is a fixed line. 

```python
def calculate_fixed_line_to_fixed_line_call_percentage(csv):
    fixed_line_to_fixed_line_call = 0
    total_from_fixed_line = 0
    for row in csv:                                                                                 <-- O(n)
        origination = is_fixed_line_number(row[initiating_telephone_number])                        <-- O(m)
        destination = is_fixed_line_number(row[receiving_telephone_number])                         <-- O(m)

        if origination is not None:                                                                 <-- O(1)
            total_from_fixed_line += 1                                                              <-- O(1)
            if destination is not None:                                                             <-- O(1)
                fixed_line_to_fixed_line_call += 1                                                  <-- O(1)
                
    percentage = 100 * fixed_line_to_fixed_line_call / total_from_fixed_line                        <-- O(1)         
    print(str("%.2f" % percentage) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
```

### Task 4:
The time complexity is O((n x n) + m) where n is reading through all the calls and m is reading through all the texts.

```python
def is_potential_telemarketers(call, texts):
    telemarketer_list = []
    for row in calls:                                                     <-- O(n)
        if row[initiating_telephone_number] not in telemarketer_list:     <-- O(a)
            telemarketer_list.append(row[initiating_telephone_number])
            
    for row in calls:                                                     <-- O(n)
        if row[receiving_telephone_number] in telemarketer_list:          <-- O(b)
            telemarketer_list.remove(row[receiving_telephone_number])
            
    for row in texts:                                                     <-- O(m)
        if row[initiating_telephone_number] in telemarketer_list:         <-- O(b)
            telemarketer_list.remove(row[initiating_telephone_number])

        if row[receiving_telephone_number] in telemarketer_list:          <-- O(b)
            telemarketer_list.remove(row[receiving_telephone_number])
    
    print("These numbers could be telemarketers: ")
    telemarketer_list.sort(key=lambda n: n.upper())                       <-- O(clogc)                       
    
    for telephone_number in telemarketer_list:                            <-- O(b)
        print(telephone_number)
```
