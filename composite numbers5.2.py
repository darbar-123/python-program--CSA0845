num1=int(input("enter the 1st number:"))
num2=int(input("enter the 2nd number:"))
print("all the composite numbers between ",num1,"and",num2)
for i in range(num1+1,num2+1):
    num=i
    count=0
    for j in range(1,num+1):
        if num%j==0:
            count+=1
            
    if count>2:
        print(num,end=" ")
