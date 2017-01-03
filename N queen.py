pl = []
fl = []
def con_pl(N):
    for i in range(2,N):
        if is_prime(i): pl.append(i)

def is_prime(n):
    for i in range(2,int(n/2+1)):
        if n%i == 0:
            return False
    return True

def is_pl(l):
    for n in l[1:]:
        if not is_prime(n):
            return False
    return True
    
def form_check(pl,it):
    for j in pl:
        p = [j]
        i = 0
        for i in range(it):
            p.append(2*p[i]+1)
            i+=1       
        if is_pl(p): fl.append(j)

N = int(input('Enter N : '))
i = int(input('Enter i : '))
con_pl(N)
form_check(pl,i)
print (fl)

        
