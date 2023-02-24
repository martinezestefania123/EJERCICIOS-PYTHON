def try_syntax(numerator, denominator):#se nombra una funcion y dentro de su parentesis se le añade dos parametros
     
    try:#try anlizara el codigo que se ingrese y si encuentra algun error comenzara a ejecutarse sus excepciones
        result = numerator / denominator#en esta variable se encuentra la operacion 
        
        print(f'In the try block: {numerator}/{denominator}/el resultado de la operacion es {result}')##con la f se le pueda agregar a un print una variable e imprime los dos argumentos 
        #quiero ver el resultado de la operacion en el print
        
        
    except ZeroDivisionError as zde:#se llama el tipo de excepcion que es ZeroDivisionError se le cambia el nombre con as y se le nombra zde
        print(zde)#imprime esta excepcion con su nombre que ya se habia cambiado
    else:# si no se encuentra el error 
        print('The result is:', result)#se imprime su resultado 
        return result#retorna el resultado 
    finally:#finaliza el programa
        print('Exiting')#imprime la frase
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 6))#imprime llamando la funcion,dentro de la funcion tendra sus parametros