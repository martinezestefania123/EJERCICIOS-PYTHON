def palabra():
    ingrese=input("digite una palabra: ")
    suma=ingrese.count("a")+ingrese.count("e")+ingrese.count("i")+ingrese.count("o")+ingrese.count("u")
    suma2=ingrese.count("b")+ingrese.count("c")+ingrese.count("d")+ingrese.count("f")+ingrese.count("g")
    suma3=ingrese.count("h")+ingrese.count("j")+ingrese.count("k")+ingrese.count("l")+ingrese.count("m")
    suma4=ingrese.count("n")+ingrese.count("p")+ingrese.count("q")+ingrese.count("r")+ingrese.count("s")
    suma5=+ingrese.count("t")+ingrese.count("v")+ingrese.count("w")+ingrese.count("x")+ingrese.count("y")+ingrese.count("z")
    sumaTotal=suma2+suma3+suma4+suma5
    
    if ingrese:
        print("esta palabra contiene este numero de vocales: ",suma)
        print("esta palabra contiene este numeor de consonates: ",sumaTotal)    
palabra()