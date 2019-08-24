# Problem Description:
## Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded here:

`
./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
`

Python's os module will be useful—in particular, you may want to use the following resources:

```python
os.path.isdir(path)
os.path.isfile(path)
os.listdir(directory)
os.path.join(...)
```
Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

```python
### Locally save and call this file ex.py ##
## Code to demonstrate the use of some of the OS modules in python
import os

## Let us print the files in the directory in which you are running this script
print (os.listdir("."))

## Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

## Does the file end with .py?
print ("./ex.py".endswith(".py"))
```

Here is some code for the function to get you started:
```python
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return None
```


# Analysis:
## Time Complexity:
The time complexity is `O(n)`. Refer Design Choices section.

## Space Complexity:
The space complexity is `O(logn)`. Additional space can be required to store the full path.

## Design Choices:
This is a recursion problem where we keep searching the directories until we find an item that matches the suffix and then append the path to our list to return.