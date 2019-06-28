p=input().split()
q=int(p[2])
a=p[0]
b=p[1]
s=0
for i in range(0,len(p[0])):
    if a[i]!=b[i]:
        s=s+1
if s==q:
    print('yes')
else:
    print('no')
