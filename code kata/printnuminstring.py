p=input()
q=[]
for i in p:
  if(i.isnumeric()):
    q.append(i)
print(*q,sep='')
