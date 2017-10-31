import collections as c

def func():
    '''
    demonstrating ordereddict

    '''

    d={}
    d1=c.OrderedDict(d)
    data='abcdefghi'
    k=0
    for x in data:
        d[x]=k
        k+=1
    print 'dictionary\n', d
    d.pop('a')
    d.pop('i')
    print 'removing a and i from dictionary\n', d
    d['a']=9
    print 'adding a with another value\n',d

func()
