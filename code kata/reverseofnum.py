p=int(input())
q=0
while(p>0):
  w=p%10
  q=q*10+w
  p=p//10
print(q)
