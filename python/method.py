# -- METODOS EN PYTHON --

# Los métodos describen el comportamiento de los objetos de una
# clase y estos representan las operaciones que se pueden llevar
# a cabo con los objetos de la clase a que pertenezca este metodo.

# La ejecucón de un metodo puede llevar a cambiar el estado de un
# objeto según dependa el caso, osea, del metodo en particular.

# Se definen de la misma forma que las funciones normales pero deben
# declararse dentro de la clase y es unabuena practica que su primer
# argumento siempre sea la palabra "self" esto para que el desarrollador
# que lea elcódigo luego no lesea complicado, self hace referencia a
# la instancia que la llama, de esta forma se afirma que los métodos
# son funciones, adjuntadas a objectos.

# Los metodos son bastante útiles, pueden ayudar con cosas como:
# iniciar sesión, cambiar contraseña, guardar archivos en una base
# de datosyentre un gran etc, es sumamente importante comprender y
# dominar las bases de los metodos.

class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludo(self):
        print("Hola!, soy {} {}."
        .format(self.nombre, self.apellido))

usuario_1 = Usuario("Yordy", "Almonte")
usuario_2 = Usuario("Bryan", "Almonte")
usuario_3 = Usuario()

usuario_1.saludo()
usuario_2.saludo()

# Con la palabra reservada "del" podemos borrar tanto instancias como atributos.
del Usuario.edad
del usuario_3



# -- METODOS ESPECIALES --

# Las clases en python cuentan con multiples metodos especiales los cuales
# se encuentran entre dobles guiones bajos "__<método>__()", 

__init__() # Siempre se ejecuta al inicio de instanciar un objeto.
    # Los argumentos que se utilizan en la definición de "__init__()"
    # corresponden a los parámetros que se deben ingresar al instanciar un objeto. 
__str__() # Se ejecuta al momento en el cual un objeto se manda a mostrar,
    # es decir es una cadena representativa de la clase, la cual puede incluir
    # formatos personalizados de presentación del mismo.
__del__() # Se ejecuta al momento en el cual un objeto es descartado por el intérprete.


