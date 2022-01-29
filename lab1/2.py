s = input()
a = 0
for x in s:
    a += ord(x)
if a > 300:
    print("It is tasty!")
else:
    print("Oh, no!")