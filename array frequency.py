def hist(l):
    d = {}
    for n in l:
        if n in d.keys():
            d[n] += 1
        else : d[n] = 1
    return d

def mk_list(d):
    l = []
    for k in d.keys():
        l.append((d[k],k))
    return l

def sort(l):
    ln = len(l)
    for i in range(ln):
        v,k = l[i]
        for j in range(i+1,ln):
            v1,k1 = l[j]
            if v > v1:
                v = v1
                (l[i],l[j]) = (l[j],l[i])
    return l
    
N = int(raw_input('Enter total no : '))
l = []
for i in range(N):
    l.append(int(raw_input()))
for k,v in sort(mk_list(hist(l))):
    for i in range(k) : print v,



