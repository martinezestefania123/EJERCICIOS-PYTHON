from  actor  import  *
import  csv
listaActores = []

with open('archivo2/o.csv') as csvDataFile :

    csvReader = csv.reader( csvDataFile )    
    for fila in csvReader :
        #print(fila)
         if len(fila)<6:
             ob=actor(fila[0],fila[1],fila[2],fila[3],fila[4])
             listaActores.append(ob)
        #imprimir(fila)
        # print('nombre:',fila[0]) 
        # imprimir('apellido:',fila[1])
        # imprimir('correo electrónico:',fila[2])
        # imprimir('id:',fila[3])
print (listaActores)
#for aprender in listaActores :
    #print (actor.getTodo())
#print(listaActores[10])