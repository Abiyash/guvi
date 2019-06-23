pqw=input()
print(' '.join(x[:1].upper() + x[1:] for x in pqw.split(' ')))
