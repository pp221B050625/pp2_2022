n = int(input())
a = ['.'] * n
for i in range(n):
    a[i] = ['.'] * n
if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            if i >= j:
                a[i][j] = '#'
elif n % 2 == 1:
    for i in range(n):
        for j in range(n):
            if i + j == n - 1 or i + j >= n:
                a[i][j] = '#'
for i in range(n):
    for j in range(n):
        print(a[i][j], end='')
    print()

