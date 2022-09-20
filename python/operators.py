# -- EXPLORANDO PYTHON: OPERADORES ARITMETICOS --

# Primero, para iniciar la consola interactiva de Python debemos
# escribir el comando **py **en Windows, pero en otros sistemas el
# comando es python3. Ahora, podemos comenzar.

# En la consola nos permite escribir operaciones matemáticas como
# 5 + 5 sin escribir nada más, pero en el editor de código debemos
# “imprimir” el resultado, de la siguiente manera:

# print(5 + 5). Con esto obtendremos el resultado.



# -- OPERADORES ARITMETICOS EN PYTHON --

a + b # Suma  
a - b # Resta
a * b # Multiplicación
a / b # División de decimales
a // b # División sin decimales
a % b # Cociente de la división
a ** b # Potenciación

# Radicación:
# El módulo math tiene diferentes funciones para realizar operaciones
# matemáticas en Python. La función sqrt() devuelve la raíz cuadrada de
# un número positivo.
import math
math.sqrt(n)

# El módulo cmath tiene métodos para lidiar con números complejos. cmath.sqrt()
# devuelve la raíz cuadrada de números negativos o imaginarios.
import cmath
cmath.sqrt(i)

# El método numpy.sqrt() puede calcular la raíz cuadrada de todos los
# elementos en un objeto de datos como una lista o un array a la vez.
# Devuelve un array que contiene la raíz cuadrada de todos los elementos.
import numpy as np
n = [9, 16, 25]
np.sqrt(n)

# La raíz cuadrada de un número no es más que el número elevado a 0.5.
# La función pow() en Python devuelve el valor de un número elevado a
# una potencia especificada y se puede usar para calcular la raíz cuadrada
# de un número como se muestra a continuación. El primer parámetro de la
# función pow() es la base y el segundo es el exponente. 
a ** 0.5
pow(a, 0.5)



# Python respeta la separación de términos, por lo que si escribimos
# 5 + 5 * 2 multiplicará primero 5 x 2. En el caso de que quisiéramos
# que primero sume 5 + 5 ponemos paréntesis: (5 + 5) * 2.

# Para recordar el orden de las operaciones en álgebra y en Python,
# es recomendable utilizar el orden PEMDAS:

#     * Paréntesis
#     * Exponentes o raíces
#     * Multiplicaciones
#     * Divisiones
#     * Adiciones y sustracciones


# -- OPERADORES LÓGICOS Y DE COMPARACIÓN EN PYTHON --

# Conoce los operadores lógicos que tiene Python y cómo utilizarlos de
# manera adecuada:



# -- OPERADORES LÓGICOS --

#     * and ( y ): compara dos valores, y si ambos son verdaderos, devuelve True.
#     * or ( ó ): si al comparar dos valores y uno de los dos se cumple, devuelve
#         True. Solo devuelve falso cuando los dos valores no se cumplen.
#     * not ( no): invierte el valor de una variable, dando el valor contrario al
#         de la variable evaluada.



# -- OPERADORES DE COMPARACIÓN --

a == b # ( igual qué ): determina si dos valores son iguales o no.
a != b# (diferente de): determina si dos valores son distintos o no. Si los valores
        #son diferentes devuelve True, si son iguales devuelve False.
a > b # (mayor que): compara dos valores, y determina si es mayor que el otro.
a < b # (menor que): compara dos valores y determina si es menor que el otro.
a >= b # (mayor o igual): compara dos valores y determinas si es mayor o igual que el otro.
a <= b # (menor o igual): compara dos valores y determinas si es menor o igual que el otro.