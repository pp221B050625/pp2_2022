n = int(input())
k = {}
lst = []
m = 0
for i in range(n):
    keyval = input().split()
    keys = keyval[0]
    value = int(keyval[1])
    if keys not in k:
        k[keys] = value
        lst.append(keys)
    else:
        k[keys] += value
    if k[keys] > m:
        m = k[keys]

lst.sort()
for j in lst:
    if k[j] < m:
        print(j, "has to receive", m - k[j], "tenge")
    else:
        print(j, "is lucky!")
