def rotated_array_search (input_list, number):
    offset = 0

    if len(input_list) == 0:
        return -2

    midpoint = len(input_list) // 2

    if input_list[midpoint] == number:
        return midpoint

    sub_list = list([])
    left_side = input_list[0:midpoint]
    right_side = input_list[midpoint:]
    
    if input_list[0] < input_list[midpoint]:
        if number >= input_list[0] and number <= input_list[midpoint]:
            sub_list = left_side
        else:
            sub_list = right_side
            offset += len(sub_list)
    else:
        if number >= input_list[midpoint] and number <= input_list[-1]:
            sub_list = right_side
            offset += len(sub_list) - 1         
        else:
            sub_list = left_side
            offset -= 1
    return offset + rotated_array_search(sub_list, number)
        

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1    

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    linear_index = linear_search(input_list, number)
    rotated_array_index = rotated_array_search(input_list,  number)
    if linear_index == rotated_array_index:
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 1, 2, 3, 4], 2])
test_function([[6, 7, 8, 1, 2, 3, 4], 3])
test_function([[6, 7, 8, 1, 2, 3, 4], 4])
test_function([[2, 3, 4, 5, 6, 7, 8, 1], 1])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])