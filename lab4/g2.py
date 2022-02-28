n = int(input())


def gen():
    num = 1
    while num < n:
        if num % 2 == 0:
            yield num
        num += 1


print(*gen(), sep=", ")