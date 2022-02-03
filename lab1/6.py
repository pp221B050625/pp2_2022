a = int(input())
i = 0
res = 0
while i < a:
    res += int(input())
    i += 1
    if res <= 10:
        print("Go to work!")
    if 10 < res <= 25:
        print("You are weak")
    if 25 < res <= 45:
        print("Okay, fine")
    if res > 45:
        print("Burn! Burn! Burn Young!")

    res = 0