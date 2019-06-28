p=[]
q=int(input())
m=input().split()
for k in m:
  p.append(k)
p.sort()
p.sort(key=len)
for k in p:
  print (k,end=' ')
