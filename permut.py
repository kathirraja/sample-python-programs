def permute(xs, low=0):
    print 'low  = ',low,'xs',xs
    if low + 1 >= len(xs): 
        print 'if  ',xs
        yield xs
    else:
        for p in permute(xs, low + 1):
            print 'xs in fp1 = ',p
            yield p        
        for i in range(low + 1, len(xs)):
            print 'xs[low]= ',xs[low],'xs[i]',xs[i]
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                print 'xs in fp2',p
                yield p        
            xs[low], xs[i] = xs[i], xs[low]

for p in permute([1,2,3]):
    print p
