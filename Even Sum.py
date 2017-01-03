import time
def find_sum(i):
        c = 0
        n = 0
        l = []
        sm = 0
        while c < i:
            if list("{0:b}".format(n)).count('1') == 2 :
                sm += n
                #print (list("{0:b}".format(n)),'  ',n)
                c+=1
            n+=1        
        return sm
            
T = int(input('Enter T : '))
t1 = time.time()
for i in range(T):
    t2=time.time()
    print (i,find_sum(i),(time.time()-t2))
print(time.time()-t1)
