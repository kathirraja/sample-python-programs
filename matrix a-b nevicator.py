mat = [['a','b','c','d','e',],
       ['f','g','h','i','j',],
       ['k','l','m','n','o',],
       ['p','q','r','s','t',],
       ['u','v','w','x','y',]]

lr = len(mat)
lc = len(mat[0])

def pos(l):
    for row in range(lr):
        if l in mat[row]:
            r = row
            for col in range(lc):
                if l == mat[r][col]:
                    c = col
                    break
            break
    return (r,c)

def moves(l1,l2):
    print l1,'->',l2
    r1,c1 = pos(l1)
    r2,c2 = pos(l2)
    r = r1-r2
    c = c1-c2
    if r < 0:
        for i in range(-r):print '\tmove down'#print -r,'times move Down'
    elif r > 0:
        for i in range(r) :print '\tmove up'#print r,'times move Up'
    if c < 0:
        for i in range(-c):print '\tmove right'#print -c,'times move Right'
    elif c > 0:
        for i in range(c) :print '\tmove left'#print c,'times move Left'
    
s = raw_input('Enter the string : ')
for row in mat:
    print row
for i in range(len(s)-1):
    moves(s[i],s[i+1])
