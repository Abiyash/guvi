pq=int(input())
if pq>0:
  for x in range(2,pq):
    if(pq%x==0):
      print("yes")
      break
  else:
    print("no")
else:
  print("yes")
