# -- LOS PRIMITIVOS: TIVOS DE DATOS SENCILLOS --

# Un objeto es una forma de modelar el mundo en programación.
# En los lenguajes de programación se caracterizan por tener métodos
# y atributos. En Python todo es un objeto.

# Podemos encontrar cuatro tipos de datos que vienen definidos por
# defecto en Python, a estos tipos de datos los conocemos como primitivos.



# -- TIPOS DE DATOS PRIMITIVOS EN PYTHON --

#     * Integers: números Enteros
#     * Floats: números de punto flotante (decimales)
#     * Strings: cadena de caracteres (texto)
#     * Boolean: boolenaos (Verdadero o Falso)

# Algunos operadores aritméticos pueden funcionar para operar con otros tipos
# de datos. Por ejemplo: podemos sumar strings, lo que concatena el texto o
# multiplicar un entero por un string, lo que repetirá el _string _las veces
# que indique el entero.

# -- TIPOS DE DATOS ADICIONALES --

#     * Datos en texto: str
#     * Datos numéricos: int, float, complex
#     * Datos en secuencia: list, tuple, range
#     * Datos de mapeo: dict
#     * Set Types: set, frozenset
#     * Datos booleanos: bool
#     * Datos binarios: bytes, bytearray, memoryview

# ¿Cómo saber el tipo de dato que estoy utilizando? Usamos el comando type(): 

x = 5
print(type(x))

# -- COMANDOS PARA CONVERTIR UN DATO A UN TIPO DIFERENTE --

int(var) # variable a entero
float(var) # variable a flotante
str(var) # variable a texto
bool(var) # variable a booleano
abs(var) # variable a valor absoluto