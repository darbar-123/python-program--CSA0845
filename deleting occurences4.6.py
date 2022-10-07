def delchar(s,c):
    if len(c)==1:
        for i in s:
            if c!=i:
                print(i,end="")
    else:
        print(s)
s=input("enter the first string:")
c=input("enter the character to be deleted:")
delchar(s,c)
