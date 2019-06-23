pq=int(input())
f=1
if pq==0 or pq==1:
  print(1)
else:
  for i in range(1,pq+1):
    f=f*i
  print(f)
