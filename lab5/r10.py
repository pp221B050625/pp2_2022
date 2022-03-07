import re

s = input()


def snake(match):
    return match.group(1).lower() + "_"


a = re.sub("([A-Z][a-z]*)", snake, s)

print(a[:-1])
