# Problem Description:
## Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is `O(log(n))`

Here is some boilerplate code and test cases to start with:

```python
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
```

# Analysis:
## Time Complexity:
The time complexity is `O(log(n))`. Refer Design Choices section.

## Space Complexity:
The space complexity is `O(1)`. No additional space is required to execute this algorithm.

## Design Choices:
I chose to alternate between finding upper and lower bounds in once iteration. This makes it slightly more efficient than finding first the upper bound in one loop and lower bound in another loop. This generally saves at least one iteration. I update the midpoint after calculating the upper and lower bounds. Then based on the value of the upper bound compared to the delta, I scale accordingly. In this case, It may reduce the upper bound by more than half in each of the first few steps saving unnecessary iterations. Once the delta gets to 0 or 1, then the answer is returned.
