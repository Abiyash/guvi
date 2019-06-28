p=int(input())
for k in range(2,p+1):
  if(p%k==0):
      s=0
      for m in range(2,k+1):
          if(k%m==0) and (m!=k):
              s=1
              break
      if(s==0):
          print(k,end=' ')
