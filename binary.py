print("Introduce 5 digitos binarios")

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

#z is the number of 0s
z = 5 - a - b - c - d - e
o = 5 - z

print("Se detectaron",o,"uno(s) y",z,"cero(s)")
