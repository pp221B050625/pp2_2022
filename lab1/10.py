s = input()
words = s.split()
i = 0
for x in words:
    if len(x) >= 3:
        print(x, end=" ")