numero = int(input("Número:"))
suma = 0
while numero != 0:
    digito = numero%10
    suma = suma + digito
    numero = numero // 10
    if suma>9 and numero==0:
        numero = suma
        suma = 0
    print(numero, digito, suma)
print(suma)
