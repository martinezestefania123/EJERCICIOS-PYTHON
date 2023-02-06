#crear un programa que contenga un contador y si su reciduo da cero que vaya contando de en uno en uno
edades = [12,15,23,30,50]
cantidad =0
for num in edades:
	if (num%3 == 0):
		cantidad+=1
print(cantidad)
