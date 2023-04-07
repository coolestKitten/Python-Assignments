import misFunciones

misFunciones.bienvenida()
a = int(input("a:"))
b = int(input("b:"))
c = misFunciones.sumar(a, b)
print("La suma es:",c)
d = misFunciones.sumar(34,a*2)
print("La suma es:",d)