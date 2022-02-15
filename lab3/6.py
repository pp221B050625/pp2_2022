s = input()
def reverse(a):
    l = [x for x in a.split()]
    l.reverse()
    for j in range(len(l)):
        print(l[j],end=" ")


reverse(s)