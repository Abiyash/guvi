p=input().split()
q=input().split()
w=input().split()
if(p[0]==q[0]==w[0] or p[1]==q[1]==w[1] or (p[0]==p[1] and q[0]==q[1] and w[0]==w[1])):
    print('yes')
else:
    print('no')
