a = int(input())
z = input()
if z == 'k':
    dec = int(input())
    res = float(a / 1024)
    print(round(res, dec))
else:
    print(a * 1024)