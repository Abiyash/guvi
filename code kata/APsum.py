p,q,w=map(int,input().split())
sum=0
for i in range(1,w+1):
 sum+=p+(w-i)*q
print(sum)
