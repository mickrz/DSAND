# Problem Description:
## Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.



# Analysis:
## Time Complexity:
The time complexity is `O(n)`. Refer Design Choices section.

## Space Complexity:
The space complexity is `O(n)`. The only space required is for each node (n).

## Design Choices:
Although there are 2 lists to read in, this can be generalized to n+m elements and reference or add to the hashmap in constant time. The only difference between intersection and union methods conceptually is to check if the element value exists in the hash map and add it if it getting the union. For the intersection, then just mark it as in both lists if it already exists.