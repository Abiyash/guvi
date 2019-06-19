pq=list(input())
if len(pq)%2==0:
  pq[int(len(pq)/2)]='*'
  pq[int(len(pq)/2)-1]='*'
else:
  pq[int(len(pq)/2)]='*'
for w in range(0,len(pq)):
  print(a[w],end='')
