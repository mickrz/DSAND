def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    ints_len = len(ints)
    min_val = None
    max_val = None
    index = 0
    
    while index < ints_len:
        if min_val is None or ints[index] < min_val:
            min_val = ints[index]
            
        if max_val is None or ints[index] > max_val:
            max_val = ints[index]
        index += 1
    return (min_val, max_val)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((0, 999) != get_min_max(l)) else "Fail")
print ("Pass" if ((-9, 0) != get_min_max(l)) else "Fail")