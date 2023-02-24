def edad():#se nombra una funcion
    try:#try anlizara el codigo que se ingrese y si encuentra algun error comenzara a ejecutarse sus excepciones
        tuedad=int(input("introduce tu edad"))#se crea un inputdonde solo se puedan agregar los valores numericos
        print(f'tu edad es  {tuedad}')##con la f se le pueda agregar a un print una variable e imprime los dos argumentos 
        #print('Tu edad es ',tuedad)
    except ValueError as e:#se llama el tipo de excepcion que es ValueError se le cambia el nombre con as y se le nombra zde    
        print(e)#imprime esta excepcion con su nombre que fue cambiado
        print("La edad debe ser un valor numerico...")#si se encuentra esta excepcion imprimira este codigo
        edad()#se invoca a la misma funcion dentro de ella para que se repita hasta que la edad sea valor numerico

edad()#se invoca la funcion