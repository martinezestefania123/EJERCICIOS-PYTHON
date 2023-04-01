#Escribe un programa   que calcule cuantos dias faltan para navidad .
#Deberas utilizar la  funcion data del modulo datatime y la fecha de navidad como referencia.
from datetime import data

hoy = data.today()
navidad_año_proximo = data(2023, 12, 25)
faltan = navidad_año_proximo - hoy
print ("Hoy:", hoy)
print ("La navidad del 2023", navidad_año_proximo)
print ("Faltan", faltan.days, "días")



#Crea una funcion que reciba que reciba como parametros una fecha de nacimiento y la fecha actual
# que devuelva la edad de la persona en años completos.
from datetime import data

def calcular_edad_años(fecha_nacimento):
    fecha_actual=data.today()
    resultado=fecha_actual.year  - fecha_nacimento.year
    resultado-=((fecha_actual.mont,fecha_actual.day)<(fecha_nacimento.month,fecha_nacimento,day))
    return resultado

fecha_nacimento_kerly =data(2000,8,28)
edad=calcular_edad_años(fecha_nacimento_kerly)

print(f'la edad de kerly es de {edad} años.')





# Escribe  un programa que solicite el usuario que introduzca una fecha en formato dd/ mm/aaaa, 
#la convierta a un objeto  de la clase date del mundulo datatime y muestre por pantalla el dia de la semana correspondiente.

"""from datetime import data
print("Fecha", fecha1, 
      "Año, nº sem., día sem.:", 
      datetime.isocalendar(fecha1))




# Escribe una fecha en formato ISO

from datetime import date
date.fromisoformat('2019-12-04')"""