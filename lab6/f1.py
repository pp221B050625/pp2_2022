import os
dirs = []
files = []
path = 'D:/'

print("ALL:",os.listdir(path))

for a in os.listdir(path):
    if os.path.isdir(os.path.join(path,a)):
        dirs.append(a)
    else:
        files.append(a)



print("DIR:",dirs)
print("FILES:",files)