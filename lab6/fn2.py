s = "String"
upp = 0
lw = 0
for i in s:
    if i.isupper():
        upp += 1
    else:
        lw += 1
print(upp)
print(lw)