w=input()
r=0
for i in w:
  if((i=='0')|(i=='1')):
    r=r+1
if(r==len(w)):
  print("yes")
else:
  print("no")
