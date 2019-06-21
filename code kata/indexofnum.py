p=int(input())
q=list(map(int,input().split()))
w=q[:]
w.sort()
for i in range(0,len(q)):
  if(q[i]!=w[i]):
     print(i)
     break
