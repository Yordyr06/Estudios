# -- CONSTRUYENDO EL CAMINO DE UN PROGRAMA CON CONDISIONES --

# Los condicionales son decisiones que se establecen desacuerdo a
# los parámetros que indiquemos, para obtener un tipo de resultado
# deseado.

# Ejemplo: si un número es mayor o igual que otro, los números deberán
# sumarse, de lo contrario deberán restarse. Debe cumplirse una condición
# para saber cuál será el camino a seguir.

# A continuación veremos cómo funcionan los condicionales en Python.



# -- EN LENGUAJE NATURAL (ESPAÑOL) --

# Si’ introduce una oración en la que se indica una condición real o hipotética
# que se ha de cumplir necesariamente para que sea cierto o se produzca lo que
# se expresa: Si corres, lo alcanzarás.

# ‘Sino’ es una conjunción adversativa que se escribe en una sola palabra y se usa,
# principalmente, para contraponer un concepto a otro: No estudia, sino que trabaja.

# ‘Si no’** introduce una oración condicional: Si no estudias, no aprobarás.



# -- COMANDOS Y EJEMPLOS --


# La forma común de codificarlos es la siguiente:
if x > y:
    print("x es mayor que y")
elif x < y:
    print("x es menor que y")
else:
    print("x es igual a y")

# También pueden escribirse en la misma linea para cuando se necesitan hacer
# comparaciones rapidas, a eso se le conoce como ifs, elifs o else cortos:
if x >= y: print("x es mayor o igual que y")
elif x <= y: print("x es menor o igual que y")
else: print("x es distinto de y")

# También se puede escribir tanto el if, como los elif y el else en la misma linea,
# a esto se le conocen como if ternarios:
print("x es igual a y") if x == y else print("x es distinto de y")

# Por otro lado cuando se necesite evaluar más de una condición requeriremos los
# operadores de AND y OR:
if x > y and x != y: print("x es mayor y distinto a y")
elif x < y or x != y : print("x es menor o distinto y")
else: print("x es igual a y")

# if: (Si) se usa para la condición principal.
# elif: (Si no) en caso de que la condición principal o anterior no se cumpla,
#       se puede utilizar para agregar otra condición.
# else: (Sino) en caso de que la(s) condición(es) anterior(es) no se cumplan,
#       e ejecuta como alternativa sin condicional.
# and: (Y) se usa para agregar una o más condiciones que funcionara igual que
#       el operador logico AND
# or: (O) Se usa para agregar una o más condiciones que funcionara igual que el
#       operdor logico OR