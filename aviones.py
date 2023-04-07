import random
import math
x1 = 0
y1 = 0
r1 = 3
x2 = -7
y2 = 0
r2 = 3
d = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
if r1+r2 >= d:
    print("Sí hay colision")
else:
    print("NO hay colision")
