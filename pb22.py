#Probleme 22
def solve_faux():
    f=open('p022_names.txt','r')
    t=0
    h=0
    for l in f:
        k=0
        t+=1
        for i in l:
            k+=ord(i)-96
            h+=k*t
    return h

buffer=[]
for line in open('p022_names.txt','r'):
    buffer.append(line)

liste=str.split(buffer[0],'","')
liste[0]='MARY';liste[-1]='ALONSO' #J'enleve les guillements du debut et de la fin
liste=sorted(liste) #Je trie la liste par ordre alphabétique
def solve():
    t=0
    h=0
    for l in liste:
        k=0
        t+=1
        for i in l:
            k+=ord(i)-64
            h+=k*t
    return h
    
def extract(filepath):
    name_list = []
    for line in open(filepath,'r'):
        for almost_name in line.split(','):
            name_list.append(almost_name[1:len(almost_name)-1])
    return name_list
def value(name):
    offset=ord('A')-1
    return sum(ord(c)-offset for c in name)
assert(value('COLIN')==53)
def solve(filepath):
    ans=0
    for index, name in enumerate(sorted(extract(filepath))):
        ans+= value(name) * index
    return ans
