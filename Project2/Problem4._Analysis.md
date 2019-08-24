# Problem Description:
## Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.


# Analysis:
## Time Complexity:
The time complexity is `O(n)`. Refer Design Choices section.

## Space Complexity:
The space complexity is `O(n)`. The only space is required for each node (n).

## Design Choices:
This is another example of recursion and creating a tree effectively under which users belong to a group or groups like a child_user belongs to the child and parent groups. Searching requires recursively going through each group to find if the user exists or not. Adding a user to a group is constant time.
