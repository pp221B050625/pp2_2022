import re

s = input()


def b(match):
    return match.group(1) + " "


a = re.sub("([A-Z][a-z]*)", b, s)

print(a)
