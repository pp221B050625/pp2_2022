n = int(input())


def gen():
    num = n
    while num >= 0:
        yield num
        num -= 1


for i in gen():
    print(i, end=" ")