i=1
suma=0
print("introduce una serie de numeros.\Si es 0 entenderemos que has\ terminado la lista", end="\n")

print("numero",i,":", end="")
numero=eval(input())
print(numero)
suma=suma+numero

while numero!=0:
    i=i+1
    print("numero",i,":", end="")
    numero=eval(input())
    print(numero)
    suma=suma+numero
print("la suma de todos los numero es: ",suma)
    
