class Persona:#se nombra una clase 
    def __init__(self,nombre,documento):#con el metodo __init__ empezamos a crear la clase. Con self decimos que nos ubicamos en la clase Persona y le pasamos un parametro a esa clase
        self.__nombre=nombre##En el parametro le agregamos un valor
        self.__documento=documento#En el parametro le agregamos un valor
    def getNombre(self):#Para mostrar el parametro utilizamos el get y entre parentesis self, que nos ubica en la clase.
        return self.__nombre#reetornamos el parrametro de nuestra clase
    def getDocumento(self):#Para mostrar el parametro utilizamos el get y entre parentesis self, que nos ubica en la clase.
        return self.__documento#reetornamos el parrametro de nuestra clase
    def setNombre(self,nombre):#para poder cambiar los datos de nuestro parametro se agrega el set,entre parentecis con elself nos podemos ubicar en la clase personaa y se le añadde el parametro 
        self.__nombre=nombre#reetornamos el parrametro de nuestra clase
    def setDocumento(self,documento):#para poder cambiar los datos de nuestro parametro se agrega el set,entre parentecis con elself nos podemos ubicar en la clase personaa y se le añadde el parametro
        self.__documento=documento#reetornamos el parrametro de nuestra clase