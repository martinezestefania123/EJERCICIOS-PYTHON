class Persona: #se crea una clase llamada persona 
    def __init__(self,nombre): # se crea una funcion con el constructor y su parametro self, tambien se pone otro parametrro nombre
        yo mismo. __nombre=nombre #se inicializa el parametro
        #print('Constructor Activado')        

    def getNombre(self): #se crea una funcion con el argumento self
        Volver a sí mismo. __nombre #se retorna el nombre de maria

    def setNombre(self,nombre): #se crea a funcion con argumentos self y nombre
        yo mismo. __nombre=nombre #se inicializa el parametro
        
class Aprendiz(Persona): #se crea a clase aprendiz herendando de la clase persona 
    def __init__(self,nombre,ficha): #se crea una funcion con los parametros
        Persona. __init__(self,nombre) # se hereda de persona
        yo mismo. __ficha=ficha #se inicializa el parametro
        

    def getFicha(self): #se crea la funcion get
        Volver a sí mismo. __ficha #se retorna la ficha
    
class documento(Persona): #se crea la clase documento heredando de persona  
    def __init__(self,nombre,documento): #se crea la funcion con los parametros 
        yo mismo. __documento=documento #se inicializa el parametro
    def getdocumento(self): #se crea la funcion 
        Volver a sí mismo. __documento #se retorna el documento

    def setdocumento(self,documento): #se crea la funcion 
        yo mismo. __documento=documento #se inicializa el parametro

clase todo(Persona):
    def __init__(self,nombre,documento,ficha):
        yo mismo. __nombre=nombre
        yo mismo. __documento=documento
        yo mismo. __ficha=ficha
    def gettodo(self):
        Imprimir (Self. __nombre, yo mismo. __documento, yo. __ficha)




app=todo("pedro" ,12345, 256)
imprimir(app. gettodo()) 