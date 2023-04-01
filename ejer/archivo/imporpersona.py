from Persona import *#se importa la clase persona
#from Curso import * ...en caso de composición
class Aprendiz(Persona):#se crea una herencia de persona que es aprendiz,en el parentesis se encuentra su clase padre que es persona
    def __init__(self,ficha,nombre,documento):#con el metodo __init__ empezamos a crear la clase. Con self decimos que nos ubicamos en la clase aprendiz y le pasamos sus parametros a esa clase
        Persona.__init__(self,nombre,documento)#tambien se le añade lo que se va a heredar de la clse padre, con todos sus parametros,que se encuentran en esa clase 
        self.__ficha=ficha#a el parametro le agregamos un valor
        self.__cursos=[]#se crea una lista vacia
    def getFicha(self):#Para mostrar el parametro utilizamos el get y entre parentesis self, que nos ubica en la clase.
        return self.__ficha#
    def setNombre(self,ficha):#Para mostrar el parametro utilizamos el get y entre parentesis self, que nos ubica en la clase.
        self.__ficha=ficha
    def agregarCurso(self,curso):#Para mostrar el parametro utilizamos el get y entre parentesis self, que nos ubica en la clase.
        #c=Curso('python',120) 
        self.__cursos.append(curso)
    def getCursos(self):
        return self.__cursos