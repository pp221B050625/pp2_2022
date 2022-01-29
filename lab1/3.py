s = input()
def tolowercase():
    for x in s:
        if ord(x) >= 65 and ord(x) <=90:
            print(chr(ord(x)+32),end="")
        else:
            print(x,end="")
tolowercase()