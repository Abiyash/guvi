w=int(input())
t=list(map(int,input().split()))
x=0
for i in range(len(t)):
  x+=t[i] 
print(x//w)
