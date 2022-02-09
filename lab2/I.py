n = int(input())
s = []
t = []
act = []
for i in range(n):
    a = input().split()
    if a[0] == "1":
        s.append(a[1])
        last = a[1]
    if a[0] == "2":
        t.append(s[0])
        s.pop(0)

for j in range(len(t)):
    print(t[j], end=" ")

