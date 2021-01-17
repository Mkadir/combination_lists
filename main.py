from itertools import combinations
from texttable import Texttable
l =[]
a = int(input("Enter N:"))
b = int(input("Enter K:"))
for j in range(1,a+1):
    l.append(j)
lsi = []
for i in combinations(l,b):
    lsi.append(list(i))
    # print(i)
t = Texttable()
t.add_rows(lsi)
print(t.draw())
print("Combination lists number ", len(lsi))
