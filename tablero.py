def mostrar(temas):
#        dep  his mus geo
#temas = [200,200,200,200]
    print("            Categorías")
    print("   1         2       3        4   ")
    print("Deportes Historia Música Geografía")


    for val in range (200,1400,200):
        #depor
        if val >= temas[0]: print(str(val).center(8), end="")
        else: print(" "*8, end="")
        #hist
        if val >= temas[1]: print(str(val).center(8), end="")
        else: print(" "*8, end="")
        #mus
        if val >= temas[2]: print(str(val).center(8), end="")
        else: print(" "*8, end="")
        #geo
        if val >= temas[3]: print(str(val).center(8))
        else: print(" "*8)
