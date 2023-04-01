#crear un directorio recursivo en el directorio creado anteriormente
import os
os.makedirs("directorio/directorio2")
os.chdir("directorio")
print(os.listdir()) 