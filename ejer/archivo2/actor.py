class actor:
    def __ini__(self,indice,año,edad,nombre,pelicula):
        self.__indice=indice
        self.__año=año
        self.__edad=edad
        self.__nombre=nombre
        self.__pelicula=pelicula

    def getTodo(self):
        return self.__indice,self.__año,self.__edad,self.__nombre,self.__pelicula
    
        