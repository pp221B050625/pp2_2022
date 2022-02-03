n, f = map(int, input().split())


def is_not_prime(n):
    return 2 not in [n, 2 ** n % n]


if n <= 500 and is_not_prime(n) is False and f % 2 == 0:
    print("Good job!")
else:
    print("Try next time!")
