values = (1, 0)#se añade una tupla
#x,y=10,12
#print(divmod(10,3))
try:#try anlizara el codigo que se ingrese y si encuentra algun error comenzara a ejecutarse sus excepciones
    q, r = divmod(*values)#q y r se vuelven variables de los elementos que tenga 
    #la tupla con la funcion divmod se le van a dar los valores que tiene la tupla,para que cada uno tome su valor posicional se coloca el asterisco
    #print('valor de q=',q)
    print(f'q={q}')#con la f se le pueda agregar a un print una variable
    print(f'r={r}')#con la f se le pueda agregar a un print una variable
except (ZeroDivisionError, TypeError) as e:##se llama el tipo de excepcion que es ZeroDivisionError con otra excepcion se le puuede añadir varas 
    #excepciones en una sola linea de codigo mientras esta este en un parentesis se le cambia el nombre con as y se le nombra "e"
    print(type(e), e)#el type muestra el tipo de error y lo imprime  