import collections as c

def midpoint(a,b):
    '''
    find mid point of line AB A--a B--b

    '''
    P=c.namedtuple('Point','x y')
    A=P(a[0],a[1])
    B=P(b[0],b[1])
    mid=P((A.x+B.x)/2,(A.y+B.y)/2)
    print mid
midpoint((1,0),(3,0))
