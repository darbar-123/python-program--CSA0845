def editdistance(str1,str2,m,n):
    if m==0:
        return n
    if n==0:
        return m
    if str1[m-1]==str2[n-1]:
        return editdistance(str1,str2,m-1,n-1)
    return 1+min(editdistance(str1,str2,m,n-1),
                 editdistance(str1,str2,n,m-1),
                 editdistance(str1,str2,m-1,n-1))
str1="cat"
str2="cut"
print(editdistance(str1,str2,len(str1),len(str2)))
