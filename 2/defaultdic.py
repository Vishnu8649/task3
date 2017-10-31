import collections as c

def default():

    '''
    demonstrating working of default dict

    '''

    d={1:'a', 2:'a', 3:'b', 4:'c',5:'d', 6:'c'}
    print 'Before reversal', d
    new=c.defaultdict(list)
    for k,v in d.items():
        new[v].append(k)
    print 'Reversed dictionary is', dict(new)

default()
