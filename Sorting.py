string= input("Enter the String")
o=[]
e=[]
u=[]
l=[]
r=[]
for x in string:
    if x.isnumeric():
        x=int(x)
        if x%2==0:
            e.append(x)
        else:
            o.append(x)
    else:
        if x.isupper():
            u.append(x)
        else:
            l.append(x)

o.sort()
e.sort()
u.sort()
l.sort()

r=l+u+o+e
res=""
for i in r:
    res=res+str(i)
print(res)