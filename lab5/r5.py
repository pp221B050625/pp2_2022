import re

s = input()

a = re.search("a.+b$",s)

if a:
    print("match")
else:
    print("no match")