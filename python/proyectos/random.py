# -- PROYECTO: VIDEOJUEGO --

# Para el siguiente ejemplo, utilizaremos módulos en Python para
# crear la funcionalidad de nuestro código. Un módulo es un archivo
# con funciones ya predefinidas, que tenemos disponibles para ejecutarlas.
# Para traer o invocar un módulo, debemos escribir lo siguiente:

# * import random
#     En este caso, “importamos” el módulo random, que trae un conjunto de
#     funciones que nos permiten trabajar con la aleatoridad.

# * numero_aleatorio = random. 
#     Gracias al punto ., accedemos a las funciones que trae el módulo.
#     En este caso, generamos una variable y le asignamos random.randint(1, 100),
#     lo cual nos genera un número aleatorio entero desde un número hasta otro
#     (en este caso del 1 al 100).



# -- EJEMPLO DE JUEGO DE ALEATORIEDAD CON MÓDULOS EN PYTHON --

import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elije un numero del 1 al 100 :"))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un numero mas grande ")
        else:
            print("Busca un numero mas pequeño ")
        numero_elegido = int(input("Elije otro numero  :"))
    import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elije un numero del 1 al 100 :"))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un numero mas grande ")
        else:
            print("Busca un numero mas pequeño ")
        numero_elegido = int(input("Elije otro numero  :"))
    print("Ganaste!")


if __name__ == "__main__":
    run()