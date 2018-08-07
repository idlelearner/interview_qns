x = [1,2,3,'a',5,6]
for i in (v for i, v in enumerate(x) if isinstance(v, int) and (v%2==1 or i%2==0)):
    print i