a = input()


def good(s):
    brackets = ['()', '{}', '[]']
    while any(x in s for x in brackets):
        for i in brackets:
            s = s.replace(i, '')
    return not s


if good(a):
    print("Yes")
else:
    print("No")