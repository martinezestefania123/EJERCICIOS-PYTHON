flujo=open('archivos/inicio.txt','a')
flujo=open('archivos/inicio.txt','a+')
#r+ hace update y lee
#a+ hace update pero no lee
#datos=flujo.read()
#print(datos)
flujo.write('\nCuando estudian con juicio')
datos=flujo.read()
print(datos)
flujo.write('\nCuando estudian con juicio----')
flujo.close()