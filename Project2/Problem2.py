import os

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
    
    path_list = list()

    try:
       dir_path = os.listdir(path) 
    except:
       return "" 
    
    for item in dir_path:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            path_list += find_files(suffix, full_path)
        elif os.path.isfile(full_path) and item.endswith(suffix):
            path_list.append(path + "\\" + item)
    
    return path_list
    

returned_path_list = find_files(".c", ".")
for item in returned_path_list:
    print(item)
    
'''
.\testdir\subdir1\a.c
.\testdir\subdir3\subsubdir1\b.c
.\testdir\subdir5\a.c
.\testdir\t1.c
'''

returned_path_list = find_files(".h", ".")
for item in returned_path_list:
    print(item)

'''
.\testdir\subdir1\a.h
.\testdir\subdir3\subsubdir1\b.h
.\testdir\subdir5\a.h
.\testdir\t1.h
'''

returned_path_list = find_files(".gitkeep", ".")
for item in returned_path_list:
    print(item)

'''
.\testdir\subdir2\.gitkeep
.\testdir\subdir4\.gitkeep
'''

returned_path_list = find_files(".c", ".\releasedir")
if len(returned_path_list) > 0:
    for item in returned_path_list:
        print(item)
else:
    print("File Not Found / Invalid directory")

'''
File Not Found / Invalid directory
'''