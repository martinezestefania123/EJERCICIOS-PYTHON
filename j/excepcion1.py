try:#try anlizara el codigo que se ingrese y si encuentra algun error comenzara a ejecutarse sus excepciones
    #print(1/1))#este impresion se le encuentra un error de sintaxis, puesto que tienne un parentisis de mas
    
    #lo que hace raise es mandar este tipo de excepsion que es syntaxError
    raise SyntaxError#lo que hace raise es mandar este tipo de excepcion que es syntaxError

except SyntaxError as e:#se llama el tipo de excepcion y con as se le cambia el nombre por uno mas corto
    
    print(e)#llama el error
    print('Cierra el parentesis')#si se encuentra el syntaxerror en el codigo,imprimira esta linea de texto

try:#try anlizara el codigo que se ingrese y si encuentra algun error comenzara a ejecutarse sus excepciones
    #raise ZeroDivisionError
    print(1/0)#se analiza esta impresion,se ve si puede tener algun tipo de error,su error es que ningun numero puedde dividirse por 0
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:#se llama el tipo de excepcion que es ZeroDivisionError se le cambia el nombre con as y se le nombra zde
    print(zde)#imprime esta excepcion con su nombre que ya se habia cambiado
    #print('prueba error')#imprime el codigo si se llega a encontar este tipo dde la excepcion