# Problem Description:
## Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:

```python
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    pass

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
```

# Analysis:
## Time Complexity:
The time complexity is `O(nlog(n))`. Refer Design Choices section.

## Space Complexity:
The space complexity is `O(n)`. Additional space is required to sort. I could have chosen other sorting algorithms such as heapsort or quicksort that would only take O(1).

## Design Choices:
Since there was no space complexity constraints, I chose to use mergesort to solve this problem. The list is sorted in ascending order and then I take generate the maximum sum numbers. Per the suggestion of the reviewer, he/she mentioned there is a way to optimize the solution up to O(n) time complexity. I believe this to be using a hashmap to count the frequencies and then use a loop to count down from 9 -> 1 since hashmap lookups are O(1) and a loop would be O(n). That would be more efficient than what I implemented. I also wanted to implement merge sort so I took that approach.