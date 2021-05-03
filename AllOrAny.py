def isPalindrome(a):
    b=str(a)
    c=b[::-1]
    if b==c and int(b)>0:
        return True
    else:
        return False

def isAllorAny(num):
    for i in num:
        if isPalindrome(i):
            return True
    return False

num=[]
i=0
n=input("Enter the numbers ")
n=n.strip()
n=n.split()
check=True
for i in n:
    if not int(i)>0:
        check=False
    x=int(i)
    num.append(x)

if check:
    print(isAllorAny(num))
else:
    print(False)