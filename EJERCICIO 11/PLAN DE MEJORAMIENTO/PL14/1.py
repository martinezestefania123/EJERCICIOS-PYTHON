edad = int(input("Dime tu edad: "))
grupo = input("Dime tu grupo [A o B]: ")

if edad >= 18 and grupo == "A" or grupo == "B":
	print("Puedes entrar")
elif edad < 18 and grupo == "A":
	print("No puedes entrar al grupo A si eres menor de edad")
elif edad < 18 and grupo == "B":
	print("Puedes entrar, pues el grupo B es para todos")
else:
	print("Elección no válida")