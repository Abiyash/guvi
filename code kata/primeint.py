p,q=input().split()
p=int(p)
q=int(q)
for n in range (p,q):
  if n>1:
    for i in range(2,n):
      if(n%i==0):
        break
    else:
      print(n,end=' ')
