def profit(l):
    sum=0
    i=1
    for i in range(0,n-1):
        if(l[i+1]>l[i]):
            sum=sum+(l[i+1]-l[i])
            i=i+1
    return sum
n=int(input("no. of elements"))
l=[]
for j in range(n):
    m=int(input(""))
    l.append(m)
print(l)
print("profit = ",profit(l))
