import re

s = input()

a = re.sub("\s|[,]|[.]",":",s)

print(a)