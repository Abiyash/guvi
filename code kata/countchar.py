w=input()
a=0
for i in range(len(w)):
  if (w[i].isdigit() or w[i].isalpha() or w[i]==' '):
    continue
  else:
    a=a+1
print(a)
