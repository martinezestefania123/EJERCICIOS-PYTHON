#hacer un programa que permita agregar al diccionario un valor y su clave
def fruits(dictionary,keys,value):
    if keys not in dictionary.keys():
        dictionary[keys] = value
        print(dictionary)
    else:
        print('existe')
di={"banana" : "banano", "strawberry" : "fresa", "apple" : "manzana"}
fruits(di,'pear','pera')
