"""
By kathir 
"""
def table(r,c):
    a = ''
    b = ''
    for i in range(0,c):
        a = a+'+----'
        b = b+'|    '
    a = a + '+'
    b = b + '|'

    for j in range(0,r):
        print a
        print b
        print b
    print a
        
        
r = int(raw_input('Enter no of row    : '))
c = int(raw_input('Enter no of column : '))
table(r,c)


 
