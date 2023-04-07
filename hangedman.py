#IMPORTAR LIBRERÍAS
import random
#VARIABLES
intentos = 7
letras = []
palabr = []
pal_ast = []
jugadores = []
jugadorGlobal = []
jugadorGanador = []
juga = []
puntaje = 0

def main():
    #DICCIONARIOS DE PALABRAS
    palabras = ["hola", "pelota", "chocolate", "computadora", "ciudad"] 
    pal = list(random.choice(palabras))

    global intentos
    global pal_ast
    global letras
    global jugadores
    global jugadorGlobal
    global jugadorGanador
    global puntaje
    global palabr
#INICIO DEL JUEGO
    print(" ")
    print("Bienvenido al juego del ahorcado")
    print(" ")
    printLogo()
    print(" ")
#ENLACES AL JUEGO
    ProgramaPideLetra(pal,intentos,puntaje)
 #VOLVER A JUGAR       
    re=input("¿Desea jugar de nuevo? ")
    if re == "si" :
        pal_ast = []
        letras = []
        jugadores = []
        main()

#JUGADORES INFO
def ProgramaPideLetra(palabra,intentos,puntaje):
    #SE INGRESA LOS NUMEROS DE JUGADORES
        print("Por favor ingrese el número de jugadores")
        num = int(input())
    #SE PEDIRÁ QUE INGRESE EL NOMBRE DE JUGADOR 
        for index in range (num):
            name = input("Ingrese el nombre del jugador " + str(index+1) + " ")
            jugadores.append(name)

#JUEGO    
        #SE ENCRIPTA LA PALABRA CON (_) SI ES UNA LETRA Y CON UN (" ") SI ES UN ESPACIO EN BLANCO
        for item in palabra:
            if item == " ":
                pal_ast.append(" ")
            else:
                pal_ast.append("_")
                
        fail = 6
        fail2 = 7
        nochange = False
        aunPuedes = True
        animo = True
        ultimo = True
        ahorcado = dibujo()

        #EMPIEZA EL CICLO DONDE SE DETERMINA EL GANADOR
        while aunPuedes:
         #DEPENDIENDO A LOS INTENTOS FALLIDOS SE IRÁ MOSTRANDO PARTE DE LA IMAGEN DEL AHORCADO
            for index in jugadores:
                if intentos == fail:              
                    print(ahorcado[7-(fail2)])    
                    fail2-=1
                    fail-=1
            #SE MUESTRA EN CONSOLA LA PALABRA O FRASE ENCRIPTADA
                print(' '.join(pal_ast))

                if animo:
                    #SE IMPRIME EL NOMBRE DEL JUGADOR
                    print("Jugador " , ((index)))
                    #SE PIDE LA LETRA
                    letra = input("Dime una letra ")             
                    letra = letra.lower()
                    #SI LA LETRA INGRESADA ESTÁ DENTRO DE LA LISTA DE LETRAS, SE MOSTRARÁ LA LEYENDA
                    if letra in letras:
                        print("Letra repetida")
                        nochange = True
                    #SI LA LETRA NO ESTÁ DENTRO DEL ABECEDARIO, SE MOSTRÁ LA LEYENDA
                    elif letra not in "abcdefghijklmnñopqrstuvwxyz":
                        print("Sólo puede ingresar una letra")
                        nochange = True
                    #EN CASO CONTRARIO SE INGRESARÁ EN LA LISTA DE LETRAS 
                    else:
                        nochange = False
                        letras.append(letra)
                
                if nochange == False:
                    #SI LA LETRA NO ESTÁ EN LA PALABRA ORIGINAL, SE LE IRÁ RESTANDO LOS INTENTOS HASTA QUE YA NO PUEDA JUGAR
                    if letra not in palabra:
                        intentos = intentos - 1
                        print('Has fallado, te quedan : ' + str(intentos))
                    #SI INTENTOS ES IGUAL A 0, SE LE NOTIFICA AL CICLO QUE SE DETENGA
                        if intentos == 0:
                            aunPuedes = False
                    #EN CASO CONTRARIO, SI LA LETRA ESTÁ EN LA PALABRA
                    #SE CAMBIARÁ EL SIMBOLO DE LA PALABRA ENCRIPTADA POR SU CORRESPONDIENTE LETRA 
                    else:
                        for var, value in enumerate(palabra):
                            if value == letra:
                                pal_ast[var] = value
                   #SI LA PALABRA ORIGINAL ES IGUAL A LA PALABRA ENCRIPTADA YA MODIFICADA SE MOSTRARA EL NOMBRE DEL GANADOR
                   #Y SE LE NOTIFICA AL CICLO QUE SE DETENGA
                if palabra == pal_ast: 
                    print("EL ganador es: " + index)
                    print('La palabra era "{palabra}"'.format(palabra=''.join(palabra)))
                    puntaje = puntaje+15
                    jugadorGanador = []
                    #EN LA LISTA DE JUGADORGANADOR SE INGRESERÁ LOS VALORES DEL NOMBRE
                    jugadorGanador.append(str(index))
                    jugadorGanador.append(puntaje)
                   #SE CREA UN ARCHIVO CON EL NOMBRE DEL JUGADOR GANADOR INGRESENADO lA LISTA CON SU NOMBRE
                    myfile=open(index+".txt", "a")
                    myfile.writelines((str(jugadorGanador)))    
                    aunPuedes = False
                    break
                #SI LOS INTENTOS LLEGAN A 0, SE LE NOTIFICA AL CICLO QUE SE DETENGA Y MUESTRA CUAL ERA LA PALABRA O FRASE A ENCONTRAR
                elif intentos == 0:
                    aunPuedes = False
                    print('Has perdido, la palabra era "{palabra}"'.format(palabra=''.join(palabra)))
                    break
                #SI LOS INTENTOS SE IGUALAN A 2, EL JUEGO DA LA OPORTUNIDAD AL USUARIO A ADIVINAR LA PALABRA
                #EN DADO CASO DE QUE ACIERTE SE MOSTRARA EL NOMBRE DEL JUGADOR GANADOR
                #SI NO ACIERTA EL JUEGO MUESTRA UN MENSAJE DE QUE YA NO TIENE MAS INTENTOS, MOSTRANDO CUAL ERA LA FRASE O PALABRA A ENCONTRAR
                elif intentos == 2 and ultimo == True:
                    animo = False
                    respu = input("¿Desea intentar escribiendo la palabra? ")
                    if respu == "si":
                        nochange = True
                        print("Jugador" , ((index)))
                        pala = input("Intenta poniendo la palabra " )
                        str1 = ''.join(palabra)
                        if pala == str1:
                            print("EL ganador es: " + index)
                            print('La palabra era "{palabra}"'.format(palabra=''.join(palabra)))
                            puntaje = puntaje+15
                            jugadorGanador = []
                            jugadorGanador.append(str(index))
                            jugadorGanador.append(puntaje)
                            aunPuedes = False
                            break
                        else:
                            intentos = intentos - 2
                    elif respu == "no":
                        nochange = False
                        animo = True
                        ultimo = False
        if(intentos == 0):
            print(ahorcado[6])  
 
#LOGO
def printLogo():
      
    print("           _                            _       ")
    print("     /\   | |                          | |      ")
    print("    /  \  | |_    __   _ _ __  _  _  _ | |   _  ")
    print("   / /\ \ | '_ \ / _ \| '_/ _ / _` |/ _` |/   \ ")
    print("  /  __  \| | | | ( ) | | |(  |( | | ( | | (_) |")
    print(" / /    \ \_| | |\_  /| | \__ \  , |\ _, |\___/ ")
                                                
#GRÁFICO
def dibujo():
    AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']    
    return AHORCADO

main()