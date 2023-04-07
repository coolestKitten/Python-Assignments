d = 1
p = 0

c = 1
m = 0

while  d != 0:
    d = int(input())
    if d == p:
        c = c + 1
    else:
        c = 1
        
        
    m = max(c,m)
    p = d
    
print (m)
        

    




