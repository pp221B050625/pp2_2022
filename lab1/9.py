a = int(input())
i = 0
while i < a:
    s = input()
    if "@gmail.com" in s:
        print(s.replace("@gmail.com",""))
    i += 1