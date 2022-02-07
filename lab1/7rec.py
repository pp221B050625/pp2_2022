a = int(input())


def to_decimal(n):
    if not n:
        return 0
    return to_decimal(n//10) * 2 + int(n % 10)


b = to_decimal(a)
print(b)