import math
import cmath

def suma():
    a = input("Ingrese un valor: ")
    b = input("Ingrese otro valor: ")

    # Validation
    try:
        a = int(a) or float(a)
        b = int(b) or float(b)
    except:
        a = str(a)
        b = str(b)

    if a != int or float: print("El valor de {} es incorrecto".format(a))
    elif b != int or float: print("El valor de {} es incorrecto".format(b))
    else:
        c = a + b
        print("La suma de {} más {} da como resueltado el número {}".format(a,b,c))


def resta():
    a = input("Ingrese un valor: ")
    b = input("Ingrese otro valor: ")

    # Validation
    try:
        a = int(a) or float(a)
        b = int(b) or float(b)
    except:
        a = str(a)
        b = str(b)

    if a != int or float: print("El valor de {} es incorrecto".format(a))
    elif b != int or float: print("El valor de {} es incorrecto".format(b))
    else:
        c = a - b
        print("La resta de {} menos {} da como resueltado el número {}".format(a,b,c))


def mult():
    a = input("Ingrese un valor: ")
    b = input("Ingrese otro valor: ")

    # Validation
    try:
        a = int(a) or float(a)
        b = int(b) or float(b)
    except:
        a = str(a)
        b = str(b)

    if a != int or float: print("El valor de {} es incorrecto".format(a))
    elif b != int or float: print("El valor de {} es incorrecto".format(b))
    else:
        c = a * b
        print("La multiplicación de {} por {} da como resueltado el número {}".format(a,b,c))


def div():
    a = input("Ingrese un valor: ")
    b = input("Ingrese otro valor: ")

    # Validation
    try:
        a = int(a) or float(a)
        b = int(b) or float(b)
    except:
        a = str(a)
        b = str(b)

    if a != int or float: print("El valor de {} es incorrecto".format(a))
    elif b != int or float: print("El valor de {} es incorrecto".format(b))
    else:
        c = a // b
        d = a % b
        print("""
        La división de {} entre {} da como resueltado {}
        Y su cociente es {} .
        """.format(a,b,c,d))


def pow():
    a = input("Ingrese un valor: ")
    b = input("Ingrese el exponente: ")

    # Validation
    try:
        a = int(a) or float(a)
        b = int(b) or float(b)
    except:
        a = str(a)
        b = str(b)

    if a != int or float: print("El valor de {} es incorrecto".format(a))
    elif b != int or float: print("El valor de {} es incorrecto".format(b))
    else:
        c = a ** b
        print("El número {} elevado a {}° da como resueltado {}".format(a,b,c))


def raiz():
    a = input("Ingrese un valor: ")   

    # Validation
    try:
        a = int(a) or float(a)
    except:
        a = str(a)

    if a != int or float: print("El valor de {} es incorrecto".format(a))
    else:
        c = math.sqrt(a) or cmath.sqrt(a)
        print("La raiz cuadrada de {} da como resueltado {}".format(a,c))


def main():
    pass


if __name__ == "__main__":
    main()