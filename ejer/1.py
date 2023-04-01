class Persona:#Le asignamos un nombre a la clase que queremos crear
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento

    def setNombre(self,nombre):
        self.__nombre=nombre #El self hace referencia a la variable de instancia y despues del igual se hace referencia al parametro
    def setDocumento(self,documento):
        self.__documento=documento

ob=Persona('Maria',10213123)
print(ob.getNombre())
print(ob.getDocumento())
ob.setNombre('Ana')
print(ob.getNombre())
ob.setDocumento(19929393)
print(ob.getDocumento())



class Aprendiz(Persona):
    def __init__(self,ficha):
        self.__ficha=ficha
        

    def getTodo(self):
        return self.__nombre,self.__ficha
    

fi=Aprendiz(1002939)
print(fi.getTodo())