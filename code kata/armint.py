p,q=input().split()
p=int(p)
q=int(q)
for x in range(p,q):
  r=0
  t=x
  while(x>0):
    c=x%10
    r=r+(c**3)
    x=x//10
  if(t==r):
    print(t,end=' ')
