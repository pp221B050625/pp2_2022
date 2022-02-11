n = int(input())
a = [0] * n
for i in range(n):
    a[i] = [0] * n
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = i * j
        elif i == 0 or j == 0:
            a[i][j] = i + j
for y in range(n):
    for x in range(n):
        print(a[y][x], end=' ')
    print()
