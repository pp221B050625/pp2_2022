import os

path = 'D:/pythoncodes/text.txt'

if os.path.exists(path):
    print("exists")
    print(os.path.dirname(path))
    print(os.path.split(path)[-1])