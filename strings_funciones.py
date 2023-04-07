texto = "Hola, buen día"
print(texto.rjust(30,"-"))
print(texto.count("Hola"))
valor ="345"
if valor.isdecimal():
    print("valor contiene un entero")
else:
    print("valor NO contiene un entero")
r = input("¿Desea continuar?:")
r = r.upper()
if r == "NO":
    print("La respuesta fue NO")
if r in ["SI", "SÍ"]:   #  if valor in ['a','e',.....]
    print("La respuesta fue SÍ")

lista = texto.split()
print(lista)

texto2= "1-2-3-40-50-4444"
lista2 = texto2.split(sep="-")
print(lista2)