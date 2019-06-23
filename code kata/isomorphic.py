p, q = input().split()
co = 0
for i in range(len(p)):
  if p.count(p[i]) == q.count(q[i]):
    co += 1
if co == len(p):
  print ("yes")
else:
  print ("no")
