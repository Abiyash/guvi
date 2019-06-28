p = input()
a = []
for x in range(len(p)):
  a.append(p.count(p[x]))
x = a.index(max(a))
print (p[x])
