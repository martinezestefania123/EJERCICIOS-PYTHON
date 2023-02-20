def mayuscula_minuscula():
    palabra=input("ingrese la palabra que desea convertir: ")
    opcion=int(input("digite su opcion: "))
    if opcion==1:
        print(palabra.upper())
    if opcion==0:
        print(palabra.lower())
mayuscula_minuscula()