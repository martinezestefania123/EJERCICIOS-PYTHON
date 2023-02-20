#Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula
def ortografia():
    while True:
        print("la primera palabra que ingrese es si quieres saber si es aguda")
        print("la segunda palabra que ingrese es si quiere saber si es esdrujula")
        print("la tercera palabra que ingrese es is quieres saber si es grave")
        print("la cuarta palabra que ingrese si quiere saber sie es sobree-sdrujula")
        c=input("ingrese palabra: ")
        
        if(c[-1]==chr(225) or c[-1]==chr(233) or c[-1]==chr(237) or c[-1]==chr(243) or c[-1]==chr(250)):
            print("es aguda")
        elif(c[-2]==chr(225) or c[-2]==chr(233) or c[-2]==chr(237) or c[-2]==chr(243) or c[-2]==chr(250)):
            print("es aguda")
        else:
            print("no es aguda")
            
        while True:
            
            c=input("ingrese palabra: ")
            
            if(c[0]==chr(225) or c[0]==chr(233) or c[0]==chr(237) or c[0]==chr(243) or c[0]==chr(250)):
                print("es esdruluja")
            elif(c[1]==chr(225) or c[1]==chr(233) or c[1]==chr(237) or c[1]==chr(243) or c[1]==chr(250)):
                print("es esdrujula")
            elif(c[2]==chr(225) or c[2]==chr(233) or c[2]==chr(237) or c[2]==chr(243) or c[2]==chr(250)):
                print("es esdrujula")
            elif(c[3]==chr(225) or c[3]==chr(233) or c[3]==chr(237) or c[3]==chr(243) or c[3]==chr(250)):
                print("es esdrujula")   
            else:
                print("no es esdrujula")
                
                while True:
                    
                    c=input("ingrese palabra: ")
                    
                    if c.endswith("ía"):
                        print("es grave") 
                    if c.endswith("úa"):
                        print("es grave") 
                    elif(c[-3]==chr(225) or c[-3]==chr(233) or c[-3]==chr(237) or c[-3]==chr(243) or c[-3]==chr(250)):
                        print("es grave")
                    elif(c[-4]==chr(225) or c[-4]==chr(233) or c[-4]==chr(237) or c[-4]==chr(243) or c[-4]==chr(250)):
                        print("es grave") 
                    else:
                        print("no es grave")
                        
                    while True:
                        
                        c=input("ingrese palabra: ")
                        
                        if(c[0]==chr(225) or c[0]==chr(233) or c[0]==chr(237) or c[0]==chr(243) or c[0]==chr(250)):
                            print("es sobre-esdrujula")
                        elif(c[1]==chr(225) or c[1]==chr(233) or c[1]==chr(237) or c[1]==chr(243) or c[1]==chr(250)):
                            print("es sobre-esdrujula") 
                        elif(c[2]==chr(225) or c[2]==chr(233) or c[2]==chr(237) or c[2]==chr(243) or c[2]==chr(250)):
                            print("es sobre-esdrujula") 
                        elif(c[3]==chr(225) or c[3]==chr(233) or c[3]==chr(237) or c[3]==chr(243) or c[3]==chr(250)):
                            print("es sobre-esdrujula")
                        elif(c[4]==chr(225) or c[4]==chr(233) or c[4]==chr(237) or c[4]==chr(243) or c[4]==chr(250)):
                            print("es sobre-esdrujula")
                         
                        else:
                            print("no es sobre esdrujula")
                            
                
ortografia() 

    

    
