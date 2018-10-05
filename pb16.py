#Probleme 16
def solve(n):
    k=0; t=0
    while (n//10**k)!=0 :
        t+=(n//10**k)%10
        k+=1
    return t


assert solve(2**15)==26
print(solve(2**1000))




        
