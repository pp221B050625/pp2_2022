a = [int(item) for item in input().split()]


def canReach(A, N):
    lastpos = N - 1
    for i in range(N - 1, -1, -1):
        if i + A[i] >= lastpos:
            lastpos = i
    if lastpos > 0:
        print("0")
    else:
        print("1")


canReach(a, len(a))