p,q=map(int,input().split())
for x in range(1,100001):
  if((x%p==0) and (x%q==0)):
    print(x)
    break
