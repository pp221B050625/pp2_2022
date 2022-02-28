a = int(input())
b = int(input())


def square():
    num = a
    while num < b:
        yield num ** 2
        num += 1


for i in square():
    print(i, end=" ")