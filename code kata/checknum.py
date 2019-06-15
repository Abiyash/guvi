w,q=map(int,input().split())
r=list(map(int,input().split()))
for i in r:
  if(i==q):
    print("yes")
    break
else:
  print("no")
