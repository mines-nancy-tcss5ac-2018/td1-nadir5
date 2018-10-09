#projet euler 22
L=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def solve():
    f=open('p022_names.txt','r')
    P=[]
    for line in f:
        P.append(line)
    l=str.split(P[0],'","')
    l[0]=l[0][1:len(l[0])]
    l[-1]=l[-1][0:len(l[-1])-1]
    l=sorted(l)
    h=0
    for k in range(len(l)):
        A=l[k]
        h+=value(A)*(k+1)
    return(h)

def value(name):   
        s=0
        for i in range(len(name)):
            a=0
            while word[i]!=L[a]:
                a+=1
            s+=a+1 
        return(s)


assert solve()==871198282
