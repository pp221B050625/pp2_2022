a = []
b = []
while True:
    f = int(input())
    if f == 0:
        break
    a.append(f)
while a:
    b.append(a[0] + a[-1])
    a.pop(0)
    a.pop(-1)
    if len(a) == 1:
        b.append(a[0])
        break


for x in b:
    print(x, end=" ")
