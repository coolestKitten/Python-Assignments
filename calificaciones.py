n = int(input())

c = 0

m = 0

s = 0

while c < n:
    b = int(input())
    s = s + b
    m = max(m, b)
    c = c + 1
    if c == n:
        a = s / n

        print (a)
        print (m)
        
    

