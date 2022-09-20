#  -- GESTOR DE ARCHIVOS EN PYTHON, FUNCIÓN "OPEN()" --

# Python nos proporciona una herramienta con la cual poder
# leer archivos si así lo requerimos y esta es la función "open()"
# cuando llamamos esta funcióny le indicamos como parametro el nombre
# del archivo que deseamos abrir luego llamamos elmetodo ".read" para
# leerlo para así entonces al ejecutar nos abrirá todo archivo dentro
# de la terminal donde ejecutemos el archivo.

# Pero esto no siempre es del todo eficiente, por ejemplo, ¿qué ocurriría
# si abrimos un archivo de masiado extenso? pues comprometería los recursos
# del equipo, por eso también se cuenta con el metodo ".readline()"

# Existen argumentos que si se lo pasamos a la función de open podremos 
# editar el archivo desde la consola, estos argumentos son:
#   * "r" (read): es el argumento por defecto, por lo tanto podemos obviarlo
#       pero si deseamos ser explicitos podemos escribirlo.
#   * "a" (append): este argumento nos ayudara cuando querramos agregar contenido
#       al archivo al final del mismo extendiendo su contenido. 
#   * "w" (write): este argumento sirve para editar el contenido del archivo a
#       nuestro antojo. En caso de que el archivo no exista lo creara.
#   * "x": este argumento nos permite crear un archivo.

# -- COMANDO BÁSICOS PARA GESTIONAR ARCHIVOS --

# Abriendo y leyedo archivos con .read()
x = open("prueba1.txt")
print(x.read())

# Simplemente para hacer espacio
print()
print()
print()

# Abriendo y leyedo archivos con .readline()
z = open("prueba2.txt")
print(z.readline())
print(z.readline())

# Simplemente para hacer espacio
print()
print()
print()

# Abriendo y leyedo archivos con iteraciones()
y = open("prueba3.txt")
for i in y:
    i = (y.readline())
    print(i)

# Cerrar archivos. Es una buena practica cerrar todos los archivos que se abrieron
# previamente.
x.close()
z.close()
y.close()