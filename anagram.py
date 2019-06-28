p=int(input())
q=0
w=[]
for k in range(p):
  w.append(input())
for k in range(p):
  if(sorted(w[k])==sorted('kabali')):
    q=q+1
print(q)
