string= input("Enter a string :")
c= input ("output :")
count={}
for i in string:
    if i==c:
        count+=1
    else:
        count=0
print( c, "=0",count)
