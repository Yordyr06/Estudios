# -- EXPLORANDO UN BUCLE DIFERENTE: EL CICLO FOR --

# El ciclo for es un tipo de bucle usado cuando se conozcan la
# cantidad de veces a iterar.

# Un contador es una variable que se encarga de contener valores
# que irán incrementando o decrementando cada vez que se ejecuta
# una acción que lo contenga. El incremento o decremento es llamado
# paso del contador y es siempre constante.

# Ejemplo: El marcador de un partido de fútbol, cada vez que un equipo
# anote un gol, aumenta su marcador en una unidad.

# Ejemplo 2: En las carreras de autos, cuando un vehículo pasa por la
# línea de meta, se incrementa en una unidad el número de vueltas dadas
# al circuito, o bien se decrementa el número de vueltas que faltan por realizar.

# Entonces, el incremento es siempre constante, el paso del contador no
# necesariamente puede ser una unidad, también puede incrementarse o
# decrementarse de a dos, tres, cuatro, hasta n. Es decir, puede ser cualquier
# número que conserve siempre el mismo valor durante todo el programa.

# Su sintaxis es:
variable = variable + constante # (al incrementar)
variable = variable - constante # (al decrementar)

# o de manera resumida:
variable += constante
variable -= constante

# Ejemplo:
gol_local = 0 #si anotan gol: gol_local = gol_local +1

# Consejo: Es importante inicializar en cero a la variable cuando aparezca
# a ambos lados del símbolo de asignación



# -- EJEMPLO DE BUCLE FOR EN PYTHON --

def imprimir_numero(inicio, fin):
    for inicio in range(fin+1):
        print(f'Numero: {inicio}')


def imprimir_numero_while(inicio, fin):
    while inicio <= fin:
        print(f'Numero: {inicio}')
        inicio += 1

def run():


    while True:
        print("""
        *********************************************************
        *******************N U M E R O S*************************
        """)
        inicio = int(input('Digite el número inicial para la secuencial:  '))
        print('')
        fin = int(input('Digite el número final para la secuencial: '))
        print('')

        if inicio < fin:
            imprimir_numero(inicio,fin)
        else:
            print(f'El numero inicial {inicio} debe ser ser menor al numero final {fin}.')



if __name__ == "__main__":
    run()



# -- RECORRIENDO UN STRING CON FOR --

# Recorrer un string con el ciclo For es tomar la cadena de caracteres
# y separarlas una a una. De este modo, quedaría el comando:

def run():
    frase = input("Escribe una frase: ")
    for caracter in frase:
        print(caracter.upper())

if __name__ == "__main__":
    run()

# Donde usaremos la variable frase para recorrer la frase que se escriba
# en el input. Cuando se escriba una frase, se recorrerá cambiando todas
# las letras a mayúsculas.



# -- EJEMPLOS DEL CICLO FOR PARA RECORRER STRINGS EN PYTHON --

# - PRIMER EJEMPLO:
def run():
    ## Este ejemplo imprime cada caracter de tu nombre
    nombre = input("Escribe tu nombre :")
    for letra in nombre:
        print(letra)

if __name__ == "__main__":
    run()


# - SEGUNDO EJEMPLO:
def run():
    frase = input("Escribe una frase: ")
    for caracter in frase:
        print(caracter.upper())

if __name__ == "__main__":
    run()