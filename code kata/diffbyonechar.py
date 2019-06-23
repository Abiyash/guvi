p,q=input().split()
c=0
for i in range(0,len(q)):
  if(q[i]!=p[i]):
    c=c+1
if(c==1):
  print('yes')
else:
  print('no')
