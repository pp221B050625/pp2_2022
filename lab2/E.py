a = [int(item) for item in input().split()]
n = a[0]
try: x = a[1]
except IndexError:
    x = int(input())
arr = []
b = 0
for i in range(n):
    arr.append(x + 2 * i)
for j in range(n):
    b = b ^ arr[j]
print(b)