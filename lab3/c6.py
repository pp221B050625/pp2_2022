a = [int(n) for n in input().split()]
b = []

for x in a:
    for i in range(2, x):
        b = list(filter(lambda y: y % i != 0 or y == i, a))
print(b)
