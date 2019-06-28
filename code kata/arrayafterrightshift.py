p=list(map(int,input().split()))
w=list(map(int,input().split()))
for k in range(0,p[1]):
  w=[w[-1]] + w[:-1]
print(*w,end=' ')
