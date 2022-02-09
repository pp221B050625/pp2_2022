x = []
y = []
p = [int(item) for item in input().split()]
n = int(input())
m = {}
d = []
for i in range(n):
    point = input().split()
    x.append(int(point[0]))
    y.append(int(point[1]))
close = 10000
for j in range(n):
    dist = ((p[0] - x[j]) ** 2 + (p[1] - y[j]) ** 2) ** (1 / 2)
    if dist < close:
        close = dist
    s = str(x[j]) + " " + str(y[j])
    m[s] = dist
    d.append(dist)
d.sort()
for x in d:
    for b in m:
        if m[b] == x:
            print(b)

