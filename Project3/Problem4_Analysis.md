# Problem Description:
## Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: `O(n)` does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an `O(n)` solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:

```python
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    pass

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
```

# Analysis:
## Time Complexity:
The time complexity is `O(n)`. Refer Design Choices section.

## Space Complexity:
The space complexity is `O(1)`.  No additional space is required to execute this algorithm.

## Design Choices:
For this problem, it relies on a pivot point (midpoint). While the midpoint is not equal to the endpoint, the start and end indicies are used index into the input list. Depending on the value, the indecies will be adjusted to continue sorting the list.