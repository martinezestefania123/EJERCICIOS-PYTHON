def codigos():
    
    ingrese= input("Ingresa tu mensaje: ")
    cipher = ''
    for x in ingrese:
        if not x.isalpha():
            continue
        code = ord(x) + 5
        if code > ord('z'):
            code = ord('e')
        cipher += chr(code)

    print(cipher)
codigos()