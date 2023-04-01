#eliminar la carpeta "e" entro del directorio "vocales"
import os

os.rmdir("vocales/e")
print(os.listdir())