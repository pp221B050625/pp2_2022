s = input()
words = s.split()
for x in words:
    if len(x) >= 3:
        print(x, end=" ")
