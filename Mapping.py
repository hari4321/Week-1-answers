num=input("Enter the numbers ")
num=num.strip()
num=num.split(" ")
res=[]
for i in num:
    res.append(int(i))
print(res)