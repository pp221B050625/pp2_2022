a = [int(n) for n in input().split()]


def spy_game(b):
    l = []
    word = ""
    for i in range(len(b)):
        if a[i] == 0 or a[i] == 7:
            l.append(a[i])
    for x in l:
        word += str(x)
    if "007" in word:
        return True
    else:
        return False


if spy_game(a):
    print("True")
else:
    print("False")
