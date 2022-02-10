s = input()
a = []
num1 = ""
num2 = ""
cnt = 0


def str_to_int(n):
    if "ONE" in n:
        n = n.replace("ONE", "1")
    if "TWO" in n:
        n = n.replace("TWO", "2")
    if "THR" in n:
        n = n.replace("THR", "3")
    if "FOU" in n:
        n = n.replace("FOU", "4")
    if "FIV" in n:
        n = n.replace("FIV", "5")
    if "SIX" in n:
        n = n.replace("SIX", "6")
    if "SEV" in n:
        n = n.replace("SEV", "7")
    if "EIG" in n:
        n = n.replace("EIG", "8")
    if "NIN" in n:
        n = n.replace("NIN", "9")
    if "ZER" in n:
        n = n.replace("ZER", "0")
    return n


for i in str_to_int(s):
    if i == '+':
        num2 = num1
        num1 = ""
        continue
    num1 += i

cnt = int(num1) + int(num2)


def int_to_str(numstr):
    x = str(numstr)
    if "1" in x:
        x = x.replace("1", "ONE")
    if "2" in x:
        x = x.replace("2", "TWO")
    if "3" in x:
        x = x.replace("3", "THR")
    if "4" in x:
        x = x.replace("4", "FOU")
    if "5" in x:
        x = x.replace("5", "FIV")
    if "6" in x:
        x = x.replace("6", "SIX")
    if "7" in x:
        x = x.replace("7", "SEV")
    if "8" in x:
        x = x.replace("8", "EIG")
    if "9" in x:
        x = x.replace("9", "NIN")
    if "0" in x:
        x = x.replace("0", "ZER")
    return x


print(int_to_str(cnt))
