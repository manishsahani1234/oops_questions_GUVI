n,a,b = map(int, input().split())

def nth_position(n,a,b):
    if a>= n-a:
        return n-a
    else:
        return b+1
    
print(nth_position(n,a,b))
