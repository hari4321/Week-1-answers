n=input("Enter the number of students ")
i=0
l=[]
while(i<int(n)):
    l.append([])
    a=input("Enter the name ")
    l[i].append(a)
    b=input("Enter the mark ")
    l[i].append(b)
    i=i+1

lmin=l[0][1]
slmin=l[1][1]
i=0
while(i<int(n)):
    if l[i][1]<lmin:
        lmin=l[i][1]
    i=i+1
    
i=0
while(i<int(n)):
    if l[i][1]<slmin and l[i][1]>lmin:
        slmin=l[i][1]
    i=i+1

res=[]
i=0
while(i<int(n)):
    if l[i][1]==slmin:
        res.append(l[i][0])
    i=i+1
    
res.sort()
for i in res:
    print(i)