import os

path = 'D:/0.txt.txt'
if os.path.exists(path):
    if os.path.isfile(path):
        print("exists")

        if os.access(path,os.R_OK):
            print("readable")

        if os.access(path,os.W_OK):
            print("writable")

        if os.access(path,os.X_OK):
            print("executable")