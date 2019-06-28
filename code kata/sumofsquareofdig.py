p=int(input())
sum=0
while(p!=0):
  w=p%10
  sum=sum+(w*w)
  p=p//10
print(sum)
