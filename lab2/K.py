a = input().split()
b = []
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in range(len(a)):
    for j in range(28):
        if punc[j] in a[i] and a[i] not in b:
            s = a[i]
            b.append(s[:-1])
    if len(b) <= i and a[i] not in b:
        b.append(a[i])
b.sort()
print(len(b))
for x in b:
    print(x)
