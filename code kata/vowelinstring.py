pq=input()
l=len(pq)
a=['a','e','i','o','u']
for i in range(0,l):
  if pq[i] in a:
    print("yes")
    break
else:
    print("no")
