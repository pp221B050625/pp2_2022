import re

s = input()


def camel(match):
    return match.group(1) + match.group(2).upper()


a = re.sub(r"(.*?)_([a-zA-Z])", camel, s)
print(a)
