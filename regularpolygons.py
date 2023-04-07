#datos del poligono
numLados = int(input('Cuantos lados? '))
lado = int(input('Cuanto miden los lados? '))
apotema = int(input('Cuanto mide el apotema? '))

#saca el perimetro para facilitarnos la vida
perimetro = numLados *lado

#saca el area y te la muestra
area = (perimetro * apotema)/2
print(area)

#pide altura para sacar el volumen
altura = int(input())

#saca el volumen del prisma y te lo muestra
volumenPris = area *altura
print(volumenPris)

#saca el volumen de la piramide y te lo muestra
volumenPira = volumenPris/3
print(volumenPira) 
