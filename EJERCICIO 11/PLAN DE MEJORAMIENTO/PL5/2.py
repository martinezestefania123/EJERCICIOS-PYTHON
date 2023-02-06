#crear un programa que permite añadir dos numeros y determinar cual es el numero menor 
n=int(input("Cuantos numeros se van a introducir?: "))

for i in range(0,n):
  numero = float(input("Ingrese un numero: ")) 
  numero2 = float(input("Ingrese un numero mayor: ")) 
  if numero < numero2:
        print("El numero es menor!")
  else:
        print("Gracias por su cooperacion.")
