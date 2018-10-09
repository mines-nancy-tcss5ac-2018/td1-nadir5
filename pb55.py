#projet euler 55

def palindrome(n):
    a=str(n)
    m=len(a)
    for i in range(m):
        if a[i]!=a[-1-i]:
            return(False)
    return(True)
    
def inverse(n):
    a=str(n)
    m=len(a)
    x=''
    for i in range(m):
        x+=a[-1-i]
    return(int(x))
    
def Lychrel(n):
    k=0
    a=n
    while k<50:
        if palindrome(a+inverse(a))==True:
            return(False)
        else: 
            a=a+inverse(a)
            k+=1
    return(True)
    
def solve(n):
    x=0
    for i in range(n):
        if Lychrel(i)==True:
            x+=1
    return(x)
    
assert solve(10000)==249
