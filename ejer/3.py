class producto:
    iva=0.19
    contador=0
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
        self.iva=self.precio*self.iva
        producto.contador+=1
    def getTodo(self):
        return self.nombre,self.precio,self.iva + self.precio   
    
    def setNombre(self,nombre):
        self.nombre=nombre
    def setPrecio(self,precio):
        self.precio=precio
    
va=producto('manzana',1000)
va2=producto('pera',1500)
print(va.getTodo())
print(va2.getTodo())
print(producto.contador)