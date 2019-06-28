p=int(input())
w=input()
temp1=0
q=['a','e','i','o','u']
for k in q:
  if(k in q):
    w=w.replace(k,'')
print(w[::-1])
