letra = []
puntos = []
suma = 0
n = int(input())
for i in range(n):
    l = input()
    letra.append(l)
    p = int(input())
    puntos.append(p)
palabra = input()
for n in range(0, len(palabra)):
    if palabra[n] in letra:
        index = letra.index(palabra[n])
        suma = suma + puntos[index]
print(suma)