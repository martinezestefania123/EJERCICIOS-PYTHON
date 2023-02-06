#hacer un programa que permita agragra una clave y un valor que no se encuentren en la lista
def electrodomesticos(dictionary,keys,value):
    if keys not in dictionary.keys():
        dictionary[keys] = value
        print(dictionary)
    else:
        print('existe')
di={"celular" : "phone", "televisor" : "television", "computador" : "computer"}
electrodomesticos(di,'audifonos','headphones')
