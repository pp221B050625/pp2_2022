a = []
while True:
    s = input()
    if s == "0":
        break
    a.append(s.split())

for i in range(len(a)):
    a[i].reverse()

a.sort()

for j in range(len(a)):
    a[j].reverse()

for x in range(len(a)):
    p = a[x]
    print(p[0], p[1], p[2])



