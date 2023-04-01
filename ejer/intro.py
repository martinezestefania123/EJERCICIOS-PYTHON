flujo=open('archivos/inicio.txt','a')#se crea un objeto y sen le pone un nombre,dentor tendra un metodo(donde buscara un archivo si esta dentro del disco duro)(lo que etsna adentro son los atributos que tendra ese objeto)
#datos=flujo.read()#se nombra esta variable y dentor tendra el objeto y sus atributos,se le añade un metodo,donde lo que hara es leer,la ruta que tiene es archivo
#print(datos)#3sse imprime los datos
flujo.write('\nCuando estudian con juicio')#se llama la clse y se le añade un metodo el cual hara que se pueda escribir el mensaje que tiene dentro del parentesis,se lo añade al archivo que antes tenia
datos=flujo.read()#se nombra nueamente otra variable,esta contiene el objeto y se le añade un metodo,este ahora leera los ultimos datos que se intgresaron en la anterior linea
print(datos)#imprime los datos
flujo.close()#hace el cierre del archivo
