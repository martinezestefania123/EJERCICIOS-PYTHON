#definir una funcion que permita saber cual es el multiplo del numero que se ingrese
def funcion(tam,div):
    for x in range(8,tam):
        if(x%div==0):
            print(x,'es multiplo de ',div)
        else:
            print(x,'NO es un multiplo de ',div)
funcion(80,8)
