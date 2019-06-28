p=[p for p in input().split()]
p[2]=int(p[2])
count1 = 0
for i in range(len(p[0])):
    t=p[0]
    q=p[1]
    if t[i]!=q[i]:
        count1=count1+1
if count1==x[2]:
  print ("yes")
else:
  print ("no")
