def merge_sort(input_list):
    input_list_len = len(input_list)

    if input_list_len == 1:
        return input_list
            
    midpoint = input_list_len // 2
    
    left_val = merge_sort(input_list[0:midpoint])
    right_val = merge_sort(input_list[midpoint:])
    
    sorted_list = list([])
    left_index_len, right_index_len = len(left_val), len(right_val)
    left_index, right_index = 0, 0
    
    while (len(sorted_list) != left_index_len + right_index_len):
        
        if left_val[left_index] < right_val[right_index]:
            sorted_list.append(left_val[left_index])

            if left_index == left_index_len - 1:
                sorted_list.extend(right_val[right_index:])
                right_index += right_index_len - right_index
            else:
                left_index += 1

        else:
            sorted_list.append(right_val[right_index])

            if right_index == right_index_len - 1:
                sorted_list.extend(left_val[left_index:])
                left_index += left_index_len - left_index
            else:
                right_index += 1
            
    return sorted_list
    
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return [-1, -1]
    
    sorted_input_list = merge_sort(input_list)
    sorted_list_len = len(sorted_input_list)    
    first_sum, second_sum = '', ''
    index = 0

    while index < sorted_list_len:

        first_sum_index = sorted_list_len - index - 1
        second_sum_index = first_sum_index - 1
        first_sum = f"{first_sum}{sorted_input_list[first_sum_index]}"

        if sorted_list_len - index != 1:
            second_sum = f"{second_sum}{sorted_input_list[second_sum_index]}"
        
        index += 2

    return [int(first_sum), int(second_sum)]
    

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4, 6, 2, 5, 9, 8, 7, 1], [9752, 8641]])
test_function([[3, 0, 4, 6, 2, 5, 9, 8, 7, 1], [97531, 86420]])
test_function([[], [-1, -1]])