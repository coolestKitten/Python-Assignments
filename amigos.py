x = int(input())
y = int(input())

sx = 0

sy = 0

for n in range (1, x+1):
    if x % n == 0 and n != x:
       
        sx = sx + n
        
for n in range (1, y+1):
    if y % n == 0 and n != y:
       
        sy = sy + n
        
if sx == y and sy == x:
    print('TRUE')
else:
    print('FALSE')
        
        

        
