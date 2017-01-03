import time
result = list()
def generate(string, start, end):
    current = 0 
    if start == end-1:
        result.append(string[:])
    else:
        for current in range (start, end):
            x = string[:]
            (x[start],x[current]) = (x[current],x[start])
            generate(x, start+1, end)
            (x[start],x[current]) = (x[current],x[start])

N=8
sol=0
t = time.time()
cols = range(N)
print cols
generate(cols,0,len(cols))
t2 = time.time()
t3 = t2-t
l = len(cols)
for combo in result:                     
    if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
        sol += 1
        print('Solution '+str(sol)+': '+str(combo)+'\n')  
        print("\n".join(' o ' * i + ' X ' + ' o ' * (N-i-1) for i in combo) + "\n\n\n\n")

print t3, t2-time.time()

raw_input()
