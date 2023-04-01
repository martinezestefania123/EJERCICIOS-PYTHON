class lector:
    def __init__(self,codigo_usuario,nombre,apellido,direccion,telefono,reserva,entrega):
        self.__codigo_usuario=codigo_usuario
        self.__nombre=nombre
        self.__apellido=apellido
        self.__direccion=direccion
        self.__telefono=telefono
        self.__reserva=reserva
        self.__entrega=entrega
     
                
    def getCodigo(self):
        return self.__codigo_usuario
    def getentrega(self):
        return self.__entrega,self.__reserva
    def getDatos(self):
        return self.__nombre,self.__apellido,self.__direccion,self.__telefono
        
class Estudiante(lector):
    
    def __init__(self,codigo_usuario,nombre,apellido,direccion,telefono,reserva,entrega):
       lector. __init__(self,codigo_usuario,nombre,apellido,direccion,telefono,reserva,entrega) 
                
    def datos(self):
        print('codigo del estudiante:',super(). getCodigo())
        print("datos del estudiante: ",super(). getDatos())     
        print('fecha de reserva y entrega',super().getentrega())
class Docente(lector):
    def __init__(self,codigo_usuario,nombre,apellido,direccion,telefono,reserva,entrega):
        lector. __init__(self,codigo_usuario,nombre,apellido,direccion,telefono,reserva,entrega) 
          
            
    def Datos(self):
        print('codigo del docente:',super(). getCodigo())
        print("datos del docente: ",super(). getDatos())
        print('fecha de reserva y entrega',super().getentrega())
        
print("digita la palabra docente o estudiante para que los puedas ver")        
ob=input("eres estudiante o docente: ")
ab=Docente(283838,'Maria','perez','carrera10',3664785,"3/2/3","2/4/5")      
eb=Estudiante(283838,'Maria','perez','carrera10',3664785,"4/7","2/4")
if ob=="docente":
    print(ab.Datos())
elif ob=="estudiante":
    print(eb.datos())

class Materiales:
    def __init__(self,codigo_material):
        self.__codigo_material=codigo_material
                
    def getcodigot(self):
        return self.__codigo_material

class Revistas(Materiales):
    def __init__(self,codigo_material,titulo_revista,tipo_revista,autor,edicion):
        Materiales. __init__(self,codigo_material)
        self.__titulo_revista=titulo_revista
        self.__tipo_revista=tipo_revista
        self.__autor=autor
        self.__edicion=edicion 
            
    def codigos(self):
        print('codigo de la revista es:',super(). getcodigot())
        return self.__titulo_revista,self.__tipo_revista,self.__autor,self.__edicion
        
class Libros(Materiales):
    def __init__(self,codigo_material,titulo_libro,tipo_libro,autor,edicion):
        Materiales. __init__(self,codigo_material)  
        self.__titulo_libro=titulo_libro
        self.__tipo_libro=tipo_libro
        self.__autor=autor
        self.__edicion=edicion 
            
    def codigoss(self):
        print('codigo del libro es:',super(). getcodigot())

        return "los datos del libro son: ",self.__titulo_libro,self.__tipo_libro,self.__autor,self.__edicion
    
print("digita la palabra revista o libro para que los puedas ver")        
o=input("revista o libro: ")        
t=Libros(99,'ujwswjune','iwiiw','wsiwiwn','sjsjss')
u=Revistas(101,'ieieen','ejjebe','ejejen','sjjeb')
if o=="libro":
    print(t.codigoss())
    print(ab.getentrega())
elif o=="revista":
    print(u.codigos())
    print(eb.getentrega())
    
    
class Pedido:
    def __init__(self,ID_pedido,Titulos_material,nombres):
         
        self.__ID_pedido=ID_pedido
        self.__Titulos_material=Titulos_material
        self.__nombres=nombres
                    
    def getdatt(self):
        return self.__ID_pedido,self.__Titulos_material,self.__nombres

print("datos del pedido")  
e=input("dijite e=1,d=2: ")
f=input("dijite libro=1 o revista=2: ")      
z=Pedido("ieiene","eieienen","siiwn")
print(z.getdatt())

if e=="1":
    print(ab.Datos())
    print(ab.getentrega())
    if f=="1":
        print(t.codigoss())
    if f=="2":
        print(u.codigos())
elif e=="2":
    print(eb.datos())
    print(eb.getentrega())
    if f=="1":
        print(t.codigoss())
    if f=="2":
        print(u.codigos())

class Bibliotecario(Pedido):
    def __init__(self,ID_pedido,Titulos_material,nombres):
        Pedido.__init__(self,ID_pedido,Titulos_material,nombres)
     
print(z.getdatt())        
       
  


