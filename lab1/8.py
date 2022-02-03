s = input()
t = input()
i = 0
cnt = 0
for x in s:
    if s[i] == t:
        print(i, end=" ")
        break

    i += 1
n = len(s)-1
for x in s:

    if s[n] == t and n != i:
        print(n, end=" ")
        break

    n -= 1
