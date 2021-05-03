def mult(a,b):
    return a*b

num=input("Enter the numbers ")
num.strip()
num=num.split(" ")
res=1
for i in range (len(num)):
    res=mult(res,int(num[i]))
print(res)