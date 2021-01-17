from itertools import combinations
from texttable import Texttable
l =[]
a = int(input("N ni kiriting:"))
b = int(input("K ni kiriting:"))
for j in range(1,a+1):
    l.append(j)
lsi = []
for i in combinations(l,b):
    lsi.append(list(i))
    # print(i)
t = Texttable()
t.add_rows(lsi)
print(t.draw())
print(len(lsi))
