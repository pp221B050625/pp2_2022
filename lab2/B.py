n = int(input())
m = 0
a = [int(item) for item in input().split()]
for i in range(0, n):
    for j in range(i+1, n):
        if a[i] * a[j] > m:
            m = a[i] * a[j]
print(m)
