try:#try anlizara el codigo que se ingrese y si encuentra algun error comenzara a ejecutarse sus excepciones
    #raise ZeroDivisionError
    print(1/0)#se trata de imprimir una divion por 0
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:#se llama el tipo de excepcion que es ValueError se le cambia el nombre con as y se le nombra zde 
    print(zde)#imprime esta excepcion con su nombre que ya se habia cambiado
    #print('prueba error')
    