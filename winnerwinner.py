n = int(input())
prev = 0
prevrev = 0
c = 1

p = 0
t = 0

while n != 0:
    d = int(input())
    if c < 3:
        if d == prev or d == prevrev:
            p = p + 1
            c = c + 1
        
    elif d == prev or d == prevrev:
        t = t + 1
        c = 1
    
    prevrev = prev
    prev = d
    
    n = n - 1
    
if t >= 1:
    p = p - 1

print (p)
print (t)
        
    


    
    
        