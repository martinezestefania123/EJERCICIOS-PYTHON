from Aprendiz import *#se importa la clase aprendiz
from Curso import *#se importa la clase curso

ap=Aprendiz('2560664A','Diego Suarez',123456)#se crea un objeto y se le pone un nombre,dentro de este se le añadera los valores que necesita la clase aprendiz la cula se le esta llamando,se le añade el valor de sus atributos
c1=Curso('Python Intermedio',200)#se crea un objeto y se le pone un nombre,dentro de este se le añadera los valores que necesita la clase curso la cual se le esta llamando,se le añade el valor de sus atributos
c2=Curso('Python Avanzado',200)#se crea un objeto y se le pone un nombre,dentro de este se le añadera los valores que necesita la clase curso la cula se le esta llamando,se le añade el valor de sus atributos
#print(c1.getNombre())#se imprime el valor del objeto c1 y este le imprimira lo que contenga 
ap.agregarCurso(c1)#a el objeto se le llama y se le añade un metodo,este mostrara lo que contenga dentro del objeto curso c1
ap.agregarCurso(c2)#a el objeto se le llama y se le añade un metodo,este mostrara lo que contenga dentro del objeto curso c2

for curso in ap.getCursos():#se añade un para(for) para que empience a leer los atributos que contenga el objeto con su metodo
    print(curso.getNombre())#se imprime su variable que contiene el ap.getcursos() y este mostra lo que contenga 