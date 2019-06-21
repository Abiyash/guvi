p,w=map(int,input().split())
x=[int(k) for k in input().split()]
q=[]
for l in x:
  if(l%2!=0):
    q.append(l)
print(q[w-1])
