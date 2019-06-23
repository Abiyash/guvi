p=input()
for x in range(0,len(p)):
  if (x%2==0):
    print(p[x+1],end='')
  else:
    print(p[x-1],end='')
