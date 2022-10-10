m=float(input("enter the starting number:"))
n=int(input("max number of line printed:"))
if(n>0):
    for i in range (1,n+1):
        for j in range(1,i+1):
            print(format(m,'.1f'),end=' ')
            m=m+0.1
        print()
else:
    print("enter the number of lines greater than 0")
