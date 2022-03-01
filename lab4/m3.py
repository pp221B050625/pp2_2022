import math
num = float(input())
length = float(input())

area = (num * length ** 2) / (4 * math.tan(math.pi/ num))

print(float(area))