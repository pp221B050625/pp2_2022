n = int(input())
strong = []
for i in range(n):
    s = input()
    up = 0
    lw = 0
    num = 0
    for j in range(len(s)):
        if s[j].isupper():
            up += 1
        if s[j].islower():
            lw += 1
        if s[j].isdigit():
            num += 1
    if up > 0 and lw > 0 and num > 0 and s not in strong:
        strong.append(s)
strong.sort()
print(len(strong))
for x in strong:
    print(x)