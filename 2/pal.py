import collections

def palindrome(x):
    '''
    Using deque of collection class to implement palindrome
    input==> string 
    output==> checking whether palindrome or not
    
    '''
    n=collections.deque(x)
    d=True
    while True:
        if len(n)==1:
            return True
        elif len(n)==0:
            return 'Not a string'
        if n.pop()!=n.popleft():
            return False
        else :
            d=True
    return d

print palindrome('asjgdg')
print palindrome('aaaaa')
print palindrome('malayalam')
        
print palindrome('m')
print palindrome('')
