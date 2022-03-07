import re
s = input()

a = re.search("ab{2}|b{3}",s)

if a:
    print("match")
else:
    print("no match")