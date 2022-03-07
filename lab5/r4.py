import re

s = input()

a = re.findall("[A-Z][a-z]+",s)

print(a)