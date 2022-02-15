s = input()
b = []
for x in range(len(s)):
    b.append(s[x])


def perm(a):
    if len(a) == 0:
        return []
    if len(a) == 1:
        return [a]
    p = []
    for i in range(len(a)):
        k = a[i]
        c = a[:i] + a[i + 1:]
        for n in perm(c):
            p.append([k] + n)
    return p


for p in perm(b):
    print(p)
