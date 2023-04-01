#2 ejercicio
def añobisiesto(inicio, fin):
   
    bisiestos = []
    for año in range(inicio, fin+1):
        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
            bisiestos.append(año)
            return 'Los años bisiestos son: ', bisiestos
print(añobisiesto(2000, 2022))