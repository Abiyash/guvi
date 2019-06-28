p=input()
q='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
w=''
for k in p:
  if k in q:
    a=q.index(k)
    a=a+3
    w=w+q[a]
print(w)
