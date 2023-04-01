import  csv
#with  open ( 'D:\\o.csv' ) as  csvDataFile :
with  open ('archivo2/o.csv') as  csvDataFile:    
#with open('files/people.csv') como csvDataFile:
    csvReader = csv.reader( csvDataFile )
    #imprimir(csvReader)
    for  fila  in  csvReader:
        #imprimir(fila)
        print ('indice:',fila [ 0 ])
        print ('año:',fila [ 1 ])
        print ('edad:',fila [ 2 ])
        print ('nombre:',fila [ 3 ])
        print ('pelicula',fila [4])