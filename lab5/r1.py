import re
s = input()

a = re.search("ab*",s)

if a:
    print("match")
else:
    print("no match")
