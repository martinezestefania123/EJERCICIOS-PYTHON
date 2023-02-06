#crear un programa que al ingresar una frase imprima cuales vocales tiene ese programa
frase=input("Frase: ")
print("Vocales en la frase:")
for x in "aeiou":
  if x in frase:
    print(x)    
