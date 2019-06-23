p,q=input().split()
p,q=int(p),int(q)
c=0
for i in range(p,q+1):
  w=i//2
  t=0
  for j in range(2,w+1):
    if(i%j==0):
      t=1
  if(t==0):
    c+=1
print(c)
