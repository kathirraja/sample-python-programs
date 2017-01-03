import time
def esum(n):
    s=0; c=0; i=0;
    while c<n:
        for j in range(i):
            s += ((2**(i))+(2**(j))); c+=1;
            if c==n: break
        i+=1
    return s

T = int(input('Enter T : '))
t1 = time.time()
for i in range(T):
    t2=time.time()
    print (i,esum(i),(time.time()-t2))
print time.time()-t1
