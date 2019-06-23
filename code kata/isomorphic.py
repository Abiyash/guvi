p,q = raw_input().split()
count = 0
for i in range(len(p)):
  if p.count(p[i]) == q.count(q[i]):
    count += 1
if count == len(p):
  print "yes"
else:
  print "no"
