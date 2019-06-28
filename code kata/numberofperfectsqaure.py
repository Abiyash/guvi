pw, qw =[int(i) for i in input().split()]
count =0
for i in range(qw+1):
    k = i*i
    if k in range(pw,qw):
            count+=1
print(count)
