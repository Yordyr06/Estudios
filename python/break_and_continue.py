# -- INTERRUMPIENDO CICLOS CON BREAK Y CONTINUE --

# La instrucción continue en Python devuelve el control al comienzo del
# ciclo while o ciclo for. Esta instrucción rechaza todas las declaraciones
# restantes en la iteración actual del ciclo y mueve el control de regreso a
# la parte superior del mismo.

# La instrucción break en Python termina el ciclo actual y reanuda la ejecución
# en la siguiente instrucción. En otras palabras, break rompe el ciclo entero
# mientras que continue solo rompe la vuelta actual.



# -- EJEMPLOS DE INTERRUPCIÓN DE CICLOS CON BREAK Y CONTINUE EN PYTHON --

#     - PRIMER EJEMPLO:
def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)

if __name__ == '__main__':
    run()
    

# - SEGUN EJEMPLO:
def run():
    texto= input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    run()