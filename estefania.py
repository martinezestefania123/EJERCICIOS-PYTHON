def edad():
    while True:
        
        pregunta=int(input("Es mayor de edad,digite edad: "))
     
        if pregunta>=18:
            print("es mayor de edad")    
    
        else:
            print("es menor de edad")
        
def pregunta2():
    pregunta2=int(input("eres mujer o hombre: "))   
    
    if 1==pregunta2:
        print("eres mujer")
        
    else:
        print("eres hombre")
        
def pregunta3():
            
    pregunta3=int(input("digite su edad: "))
    
    if pregunta3>=18 and pregunta3<=49:
                    print("eres aun joven")
    else:
        print("estas en la edad adulta")
                  
def contador(num1,num2):
    for i in range(num1+1,num2):
        print(i)
numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese otro numero: "))
contador(numero1,numero2)
    
def primo(num):
    for i in range(2,num):
       if num%i==0:           
           return False
    return True

 
numero=int(input("Número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")



