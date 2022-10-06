n=int(input("enter the number of elements"))
l=[]
count=0
for i in range(n):
    m=int(input())
    l.append(m)
print(l)
for j in range(len(l)):
    for k in range(j+1):
        if(l[j]==l[k]):
            count=count+1
print(count-n)
