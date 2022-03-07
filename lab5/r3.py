import re

s = input()

a = re.findall("[a-z]+_[a-z]+",s)

print(a)