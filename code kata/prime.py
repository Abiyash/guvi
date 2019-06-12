a=int(input())
if a>0:
  for x in range(2,a):
    if(a%x==0):
      print("no")
      break
  else:
    print("yes")
else:
  print("no")
