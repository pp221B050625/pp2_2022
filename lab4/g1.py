n = int(input())


def gen():
    num = 1
    while num < n:
        yield num ** 2
        num += 1


for i in gen():
    print(i)
