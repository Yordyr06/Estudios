#  -- PARADIGMA DE LA PROGRAMACIÓN ORIENTADA A OBJETO --

# Pythones un lenguje de programación de multiparadigma y dentro de esos
# paradigmas esta el de la programación orientada a objeto, este es uno de
# los paradigmas más empleados en el mundo de la programación, haciendo que
# el concepto de clases, objetos, herencias y otros más sean populares,
# eficientes y necesarios para un desarrollador. A groso modo objetos son
# un tipo que poseen atributos (tambien llamados propiedades) y metodos
# (tambien llamado comportamientos), por lo general crearemos nuestros
# objetos agrupando propiedades y metodos de forma que tengan algun sentido 
# útil para nosotros.
# 
# Las propiedades de un objeto son una especie de caracteristica que puede
# almecenar practicamente cualquier tipo de dato en su interior siempre y
# cuando conserve el sentido para el objeto en cuestion. Por otro lado los
# metodos son funciones que (valga la redundancia) van a funcionar con el
# objeto y con las propiedades del mismo.
#
# En un método podemos llamar valores del objeto y de esta forma acceder a
# sus datos para manipularlos y utilizarlos de la forma en que necesitemos
# para el beneficio de la aplicación. 



# -- CLASES Y OBJETOS EN PYTHON --

# El objeto no puede existir sin antes poseer una clase de la cual fue creado, esto
# es así porque una clase es para un  objeto lo que es un plano arquetectonico a un
# edificio, por lo que las clases pueden ser definidas como el diseño y la estructura
# del objeto antes de que resiva valores y sea un objeto como tal. Por esta razón no
# puede existir un objeto sin antes haber una clase previa de la cual nacerá este
# obejto, la particularización de esta clase, es decir, el objeto, cuando pasa a tener
# uso y ocupación real en elcodigo se convierte en una instancia.
# 
# Para declarar una clase en python ocuparemos la palabra reservada de "class" seguido
# del nombre de la clase y luego ":" a continuación se identa el código para empezar a
# definiry nombrar las propiedades o atributos de la clase. Es importante que la primera
# letra del nombre de la clase  este en mayusculas y el nombre completo de las instancias
# en minusculas porque existe un convenio de todos los lenguajes de programación donde se
# establese que la forma correcta de nombrar una clase y una instancia es la antes dicha
# y esto esuna buena practica. Veamos algunos ejemplos de clases.

# Primer ejemplo:
class Usuario:
    email = "yordyalmonte06@hotmail.com"
    apellido = "Almonte"
    nombre = "Yordy"
    edad = "25 años"
    genero = "M"

usuario = Usuario() # Esto sería la instancia.
print(usuario)
# El print(usuario) no nos mostrará los datos suministrados si no que nos indicara que "usuario"
# es una instancia de la clase "Usuario", para tener el resultado deseado debemos de hacerlo 
# de la siguiente forma:
print(usuario.email, usuario.apellido, usuario.nombre, usuario.edad, usuario.genero)
# El código pudiese ser identado por temas esteticos.

# Segundo ejemplo:
class Animal:
    tipo = "Perro"
    raza = "Pastor Aleman"
    color = "Marron"
    edad = "10 años"
    genero = "H"

animal = Animal() # Esto sería la instancia.
print(animal)
# El print(animal) no nos mostrará los datos suministrados si no que nos indicara que "animal"
# es una instancia de la clase "Animal", para tener el resultado deseado debemos de hacerlo 
# de la siguiente forma:
print(animal.tipo, animal.raza, animal.color, animal.edad, animal.genero)
# El código pudiese ser identado por temas esteticos.

# Tercer ejemplo:
class Ciudadano:
    cedula = "402-2579223-9"
    apellido = "Almonte Ruiz"
    nombre = "Yordy Leonardo"
    lugar_nacimiento = "Santo Domingo, R.D."
    nacionalidad = "República Dominicana"
    fecha_nacimiento = "06 septiembre 1996"
    estado_civil = "soltero"
    genero = "M"

ciudadano = Ciudadano() # Esto sería la instancia.
print(ciudadano)
# El print(ciudadano) no nos mostrará los datos suministrados si no que nos indicara que "ciudadano"
# es una instancia de la clase "Ciudadano", para tener el resultado deseado debemos de hacerlo 
# de la siguiente forma:
print(ciudadano.cedula, ciudadano.apellido, ciudadano.nombre,
    ciudadano.lugar_nacimiento, ciudadano.nacionalidad,
    ciudadano.fecha_nacimiento, ciudadano.estado_civil, ciudadano.genero)
# El código fue identado por temas esteticos.