import os
path = "D:/pythoncodes/lab6/file_to_del.txt"

if os.path.exists(path):
    os.remove(path)