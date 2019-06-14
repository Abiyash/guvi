p=input("")
c=0
for i in range(0,len(p)):
  if(p[i].isalpha()):
    c=c+1
    break
for i in range(0,len(p)):
  if(p[i].isdigit()):
    c =c+1
    break
if(c==2):
    print("Yes")
else:
  print("No")
