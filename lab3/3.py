heads = int(input("Enter number of heads "))
legs = int(input("Enter number of legs "))


def solve(h, l):
    c = 2 * (h - (l / 4))
    r = h - c
    print("Rabbits:", int(r))
    print("Chickens:", int(c))


solve(heads, legs)
