a = [int(n) for n in input().split()]


def has33(a):
    for i in range(len(a) - 1):
        if a[i] == 3 and a[i + 1] == 3:
            return True
    return False


if has33(a):
    print("True")
else:
    print("False")
