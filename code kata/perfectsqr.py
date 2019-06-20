p,q=list(map(int,input().split()))
w=p*q
for i in range(0,w+1):
  if(i**2==0):
    print("yes")
    break;
else:
  print("no")
