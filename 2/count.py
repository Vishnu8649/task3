import collections as c

def mostcommon(L,l):
    ''' 
        Find the most 2 common words from a string,
        print words after substracting the elements from another string
        and sort in most to least order

    '''
    d=c.Counter(L.split())
    print 'Most common 2 words are', d.most_common(2)
    f=sorted(d.items(), key= lambda (x,y):y, reverse =True)
    k=1
    print 'rank of words according to mostly used:\n'
    for x, y in f:
       print k,x
       k+=1
    d1=c.Counter(l.split())

    print '\n \ndifference of words\n'
    for x in d-d1:
        print x,

