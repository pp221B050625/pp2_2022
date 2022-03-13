import os
dirs = []
files = []
path = 'D:\pythoncodes'

print(os.listdir(path))

for a in os.listdir(path):
    if "." not in a:
        dirs.append(a)
    else:
        files.append(a)



print(dirs)
print(files)