w=int(input())
x,y=input().split()
x=int(x)
y=int(y)
if w in range(x+1,y):
    print("yes")
else:
    print("no")
