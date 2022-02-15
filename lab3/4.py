a = [int(n) for n in input().split()]
c = []

def filter_prime(b):
    for x in b:
        prime = True
        for i in range(2, x):
            if x % i == 0:
                prime = False
        if prime:
            c.append(x)

filter_prime(a)
print(c)