import math

r = int(input())
px = int(input())
py = int(input())
cx = int(input())
cy = int(input())

d = math.sqrt(pow(cx-px,2) + pow(cy-py,2))
if r == d:
    print('SOBRE')
elif r >= d:
    print('DENTRO')
else:
    print('FUERA')
    
