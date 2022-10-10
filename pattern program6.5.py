row=int(input("number of rows:"))
j=''
for i in range(row,0,-1):
    j=j+str(row+1-i)+''
    print(''*(i-1)+j[::-1])
