# -- HERENCIA --

# La herencia es un concepto de la programacion orientada
# a objeto con el que buscamos reutilizar y eficientizar todo
# el codigo que sea posible a la hora de trabajar con objetos,
# clases e instancias, puede verse como copiar los códigos de
# una clase en otra.

# La clase que hereda el código es conocida como clase hijo y
# esta clase tendrá acceso a todos los atributos y metodos que
# ha heredado. La clase que deja en herencia el código se conoce
# como clase padre y esta no podrátener acceso a los atributos ni
# a los metodos de las clases a las que deja herencia. 

# Ejemplo:
class Animal:
    def __init__(self, nombre, onomatopeya, genero):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
        self.genero = genero
    
    def saludo(self):
        print("Hola me llamo {} y soy un {}, mi onomatopeya es el {} y soy {}."
        .format(self.nombre, self.tipo, self.onomatopeya, self.genero))
    
class Gato(Animal):
    tipo = "gato"

class Perro(Animal):
    tipo = "perro"
    
class Canario(Animal):
    tipo = "pajaro"

gato = Gato("Fluffy", "mauyido", "hembra")
gato.saludo()

perro = Perro("Cyndie", "ladrido", "hembra")
perro.saludo()

canario = Canario("Piolyn", "silvido", "macho")
canario.saludo()