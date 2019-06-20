p=input()
q=""
for i in p:
  if i not in q:
    q=q+i
if(p==q):
  print("Yes")
else:
  print("No")
