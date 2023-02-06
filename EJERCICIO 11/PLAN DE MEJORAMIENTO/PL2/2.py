#definir una funcion que se ingresen dos numeros y que el programa imprima la secuencia correcta
def funcion(m,n):
    for p in range(m):
        for q in range(n):
            print(p,'-',q)
funcion(6,6)
