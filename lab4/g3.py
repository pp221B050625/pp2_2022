n = int(input())


def gen():
    num = 3
    while num < n:
        if num % 3 == 0 or num % 4 == 0:
            yield num
        num += 1


for i in gen():
    print(i, end=" ")