def caracter():
    digite=input("digite una palabra y mire cunato se repite una letra: ")
    veces=input("cunatas veces se repite: ")
    
    for x in digite:
        print(x,"se repite",x.count(veces))
caracter()