n=5
for i in range(n-1,-1,-1):
    for j in range(i):
        print(end="--")
    for j in range(n-1,i,-1):
        print("*",end="-")
    for k in range(i,n):
        if k != n-1:
            print("*",end="-")
        else:
            print("*",end="")
    for l in range(2*i):
        print(end="-")
    print()
for i in range(1,n):
    for j in range(i):
        print(end="--")
    for k in range(n-1,i,-1):
        print("*",end="-")
    for l in range(i,n):
        if l != n-1:
            print("*",end="-")
        else:
            print("*",end="")
    for m in range(2*i):
        print(end="-")
    print()