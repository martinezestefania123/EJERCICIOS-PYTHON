class Curso:#se nombra nuevamente un clase curso
    def __init__(self,nombre,horas):#con el metodo __init__ empezamos a crear la clase. Con self decimos que nos ubicamos en la clase Persona y le pasamos un parametro a esa clase
        self.__nombre=nombre#a el parametro le agregamos un valor
        self.__horas=horas#a el parametro le agregamos un valor
    def getNombre(self):#Para mostrar el parametro utilizamos el get y entre parentesis self, que nos ubica en la clase.
        return self.__nombre#reetornamos el parrametro de nuestra clase