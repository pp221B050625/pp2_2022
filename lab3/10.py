a = input().split()


def unique(list):
    l = []
    for i in range(len(list)):
        if list[i] not in l:
            l.append(list[i])
    return l


print(unique(a))
