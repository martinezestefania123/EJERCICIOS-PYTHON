class Vehiculo:#le asignamos el nombre a la clase,el cual es vehiculo
    def __init__(self,tipo):#con el metodo especial con el que se inicia el constuctor,dento se le agrega el self decimos que nos ubicmos en la clase vehiculo y se le añade un parametro
        self.tipo=tipo#esto nos permite acceder a la variable
    def descripcion(self):#se define el metodo llamado descripcion,el self nos permite ubicarnos en la clase vehiculo
        print('Soy generico no tengo descripcion',self.tipo)#se imprime lo que esta dentro del aprentesis e imprime el texto
#v=Vehiculo('Cualquier tipo')

    def getTipo(self):#Para mostrar el parametro utilizamos el get y entre parentesis self, que nos ubica en la clase.
        return self.tipo#se retorna nuevamente el atributo tipo de la clse vehiculo
        #return Vehiculo.tipo
    def __str__(self):#este metodo retorna de que clase es el objeto,y con el self nos indica que estamos en la clase vehiculo
        return 'Soy objeto de la clase Vehiculo'#retorna este texto 

class Herramienta:#le asignamos el nombre a la clase,el cual es herramienta
    def __init__(self,proposito):#con el metodo especial con el que se inicia el constuctor,dento se le agrega el self decimos que nos ubicmos en la clase herramiennta y se le añade un parametro
        self.__proposito=proposito#esto nos permite acceder a la variable
    def getProposito(self):#Para mostrar el parametro utilizamos el get y entre parentesis self, que nos ubica en la clase.
        return self.__proposito#se retorna nuevamente el atributo proposito de la clase herramienta
    def __str__(self):#este metodo retorna de que clase es el objeto,y con el self nos indica que estamos en la clase herramienta
        return 'Soy objeto de la clase Herramienta'#retorna este texto 
class Terrestre(Vehiculo,Herramienta):#con el metodo especial con el que se inicia el constuctor,dento se le agrega el self decimos que nos ubicmos en la clase terrestres y se le añade un parametro
    def __init__(self,tipo,proposito):
        Herramienta.__init__(self,proposito)
        Vehiculo.__init__(self,tipo)        
    def datos(self):
        print('Tipo: ',super().getTipo())
        print('Tipo: ',super().getProposito())
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")
t.datos()
print(t.__str__())