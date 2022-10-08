g=input("grade = ")
n=int(input("salary = "))
d=str(n)
if(g=='B'):
    if(n<=0 or d.isalpha()):
        print("enter valid salary in integer greater than 0")
    else:
        print("saalary",n)
        if(n>10000):
            print("bonus=",n*10/100)
            print("total to be paid : ",n+n*10/100)
        else:
            print("bonus = ",n*10/100+n*2/100)
            print("total to be paid : ",n+n*10/100+n*2/100)
elif(g=='A'):
    if(n<=0 or d.isalpha()):
        print("enter valid salary in integer greater than 0")
    else:
        print("salary=",n)
        if(n>10000):
            print("bonus=",n*5/100)
            print("total to be paid : ",n+n*5/100)
        else:
            print("bonus = ",n*5/100+n*2/100)
            print("total to be paid : ",n+n*5/100+n*2/100)
else:
    print("enter the grade A and B only")
