def electrodomesticos(dictionary,keys,value):
    if keys not in dictionary.keys():
        dictionary[keys] = value
        print(dictionary)
    else:
        print('existe')
di={"celular" : "phone", "televisor" : "television", "computador" : "computer"}
electrodomesticos(di,'audifonos','headphones')