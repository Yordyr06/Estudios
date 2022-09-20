# -- APRENDIENDO A NO REPETIR CODIGO CON FUNCIONES --

# Las funciones ayudan a optimizar el código. Es decir, utilizar
# la menor cantidad de líneas dentro del código y evitar escribir
# acciones repetitivas.

# Esto nos sirve para entregar un código más limpio y con buenas
# prácticas, que no desperdicia recursos innecesariamente. En Python,
# para definir funciones empleamos def.

# Gracias a def, podemos “definir” funciones que emplearemos más tarde.
# Una función, en programación, es un grupo de instrucciones con un
# objetivo en particular y que se ejecuta cuando es “invocada”.

# Cuando la definimos, estamos dándole un conjunto de instrucciones o
# un algoritmo. Al ahorrar líneas de código con funciones logramos también
# que la legibilidad de este sea más fácil.

# Para declarar funciones
def funct1():
    print("Hola Mundo")
funct1()



# -- ARGUMENTOS DE LAS FUNCIONES --

# Una gran y poderosa ventaja es que a las funciones le podemos pasar argumentos,
# los argumentos no son más que variables que le permitiran a la función ser
# flexible según la necesidad. A la hora de declarar una funcion argumentada
# esta variable resive el nombre de argumento pero al llamar la función para que
# sea ejecuta y tengamos que pasarle los datos que deseamos dicha variable pasará
# a llamarse parametro o parametros.

# Función Argumentada
def funct2(arg1):
    print(arg1)
funct2("Hola Mundo")

# Otra forma de nombrar una funciona argumentada
def funct3(arg1):
    print(arg1)
funct3(arg1 = "Hola Mundo")

# Funcion con multiples argumentos
def funct4(arg1, arg2, arg3, arg4):
    print(arg1 + arg2)
    print(arg3 + arg4)
funct4("Hola", "Mundo", "Otra", "Vez")

# Podemos utilizar los argumentos en el orden que desemos, para esto debemos indicar
# cuando llamemos nuetra función que a que parametro corresponde cada nombre.
def funct5(nombre, apellido):
    print(nombre + apellido)
funct5(apellido = "Almonte", nombre = "Yordy")

# Funcion argumentada donde el parametro que pasaremos sera una lista.
def params_list(list):
    print(list[0] + list[1])
params_list(["Hola", "Mundo"])

# Funcion argumentada donde el parametro que pasaremos sera una tupla.
def params_tupla(tupla):
    print(tupla[0] + tupla[1])
params_list(("Hola", "Mundo"))

# Función argumentada por una tupla, para esto tendremos que colocar "*" delante del
# argumento cuandodeclaremos la función.
def args_tupla(*tupla):
    print(tupla[0] + tupla[1])
args_tupla("Hola", "Mundo")

# Función argumentada por un diccionario, para esto tendremos que colocar "**"
# (es considerado una buena practica utilizar "kwagrs" en este caso porque esto
# significa "key word arguments") delante del argumento, luego nombrar las llaves y los
# valores cuando le vayamos a pasar los parametros a la función.
def args_dict(**kwagrs):
    print(kwagrs ["nombre"], kwagrs ["apellido"])
args_dict(nombre = "Yordy", apellido = "Almonte")

# Función argumentada por defecto, con esto podemos evitar tener que pasarle algún
# parametro a la función si así lo deseamos.
def arg_defecto(arg1 = "Mundo"):
    print(arg1)
arg_defecto("Hola")
arg_defecto()

# Las funciones pueden retornar resultados con la instruccion "return" para que sean
# utilizados más adelante en el codigo cuando la función sea llamada pero como es un dato
# como cualquier otro debe ser almacenado en una variable porque de lo contrario divagara
# en el código.
def funct_return(arg1, arg2):
    return arg1 + arg2
frase = funct_return("Hola", "Mundo")
print(frase)

# Función recursiva es aquella función que en su ejecusión se llama a sí misma, este tipo
# de funciones son bastante utiles cuando se quiere generar una reconeccion a un servidor
# o a una base de datos por ejemplo, por esa razón el ejemplo que vamos a verle hace un
# flaco servicio a la utilidad que pueden tener las funciones recursivas pero nos servirá
# como ejemplo practico.
def recursivity(i):
    if i < 1:
        return i
    print(i)
    recursivity(i - 1)
recursivity(5)