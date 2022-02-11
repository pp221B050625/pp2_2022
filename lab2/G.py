n_demons = int(input())
w = []
a = []
n = []
d_killed = 0
for i in range(n_demons):
    d_w = input().split()
    w.append(d_w[1])
n_hunters = int(input())
for j in range(n_hunters):
    h_a_n = input().split()
    a.append(h_a_n[1])
    n.append(int(h_a_n[2]))
for x in range(n_hunters):
    for j in range(n_demons):
        if a[x] == w[j] and n[x] > 0:
            d_killed += 1
            n[x] = n[x] - 1
            w[j] = ""

print("Demons left:", n_demons - d_killed)

