n=input("s=")
s=n[: :-1]
count=0
for i in s:
    if(i==" "):
        break
    else:
        count=count+1
print(count)
