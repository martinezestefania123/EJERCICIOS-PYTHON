class lector:
    def __init__(self,codigo_usuario,nombre,apellido,direccion,telefono):
        self.__codigo_usuario=codigo_usuario
        self.__nombre=nombre
        self.__apellido=apellido
        self.__direccion=direccion
        self.__telefono=telefono
                

    def getCodigo(self):
        return self.__codigo_usuario
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    
    def setCodigo(self,codigo_usuario):
        self.__codigo_usuario=codigo_usuario
    def setNombre(self,nombre):
        self.__nombre=nombre 
    def setApellido(self,apellido):
        self.__apellido=apellido
    def setDireccion(self,direccion):
        self.__direccion=direccion
    def setTelefono(self,telefono):
        self.__telefono=telefono

ob=lector(283838,'Maria','perez','carrera10',3664785)
print(ob.getCodigo())
print(ob.getNombre())
print(ob.getApellido())
print(ob.getDireccion())
print(ob.getTelefono())
ob.setCodigo(55566)
print(ob.getCodigo())
ob.setNombre('Ana')
print(ob.getNombre())
ob.setApellido('martinez')
print(ob.getApellido())
ob.setDireccion('carrera1')
print(ob.getDireccion())
ob.setTelefono(182838)
print(ob.getTelefono())


class Estudiante(lector):
    def __init__(self,usuario_estudiante):
        self.__usuario_estudiante=usuario_estudiante
        
    def getEstu(self):
        return self.__usuario_estudiante
    
pi=Estudiante('estudiante')
print(pi.getEstu())
        
class Docente(lector):
    def __init__(self,usuario_Docente):
        self.__usuario_Docente=usuario_Docente
        
    def getEstu(self):
        return self.__usuario_Docente
    
pi=Estudiante('Docente')
print(pi.getEstu())


