def verbo():
    while True:
        
        print("la primer palabra que ingrese es para saber si esta en futuro")
        print("la segunda palabra que ingrese es para saber si esta en presente")
        print("la tercer palabra que ingrese es para saber si esta en pasado")
        
        ingrese=input("ingrese el verbo: ")
        
        if ingrese.endswith("rá"):
            print("es una palabra en futuro")
        elif ingrese.endswith("ré"):
            print("es una palabra en futuro")
        elif ingrese.endswith("rás"):
            print("es una palabra en futuro")
        elif ingrese.endswith("rán"):
            print("es una palabra en futuro")
        elif ingrese.endswith("réis"):
            print("es una palabra en futuro")
        elif ingrese.endswith("remos"):
            print("es una palabra en futuro")
        else: 
            print("esta palabra no esta en futuro")
        
        while True:
            
            ingrese=input("ingrese el verbo: ")
            
            if ingrese.endswith("a"):
                print("es una palabra en presente")
            elif ingrese.endswith("as"):
                print("es una palabra en presente")
            elif ingrese.endswith("o"):
                print("es una palabra en presente")
            elif ingrese.endswith("os"):
                print("es una palabra en presente")    
            elif ingrese.endswith("e"):
                print("es una palabra en presente")
            elif ingrese.endswith("es"):
                print("es una palabra en presente")
            elif ingrese.endswith("y"):
                print("es una palabra en presente")
            elif ingrese.endswith("an"):
                print("es una palabra en presente")
            elif ingrese.endswith("en"):
                print("es una palabra en presente")
            else:
                print("esta palabra no esta en presente")
                     
            while True:
                ingrese=input("ingrese el verbo: ")
                
                if ingrese.endswith("é"):
                    print("es una palabra en pasado")
                elif ingrese.endswith("ó"):
                    print("es una palabra en pasado")
                elif ingrese.endswith("e"):
                    print("es una palabra en pasado")
                elif ingrese.endswith("o"):
                    print("es una palabra en pasado")
                elif ingrese.endswith("i"):
                    print("es una palabra en pasado")
                elif ingrese.endswith("os"):
                    print("es una palabra en pasado")
                elif ingrese.endswith("on"):
                    print("es una palabra en pasado")
                else:
                    print("esta palabra no esta en pasado")
verbo()