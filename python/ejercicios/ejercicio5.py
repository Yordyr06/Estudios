def mayor(usuario):
    if usuario.edad >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")

class Usuario:
    def __init__(self, edad):
        self.edad = edad

mayor(Usuario(20))
mayor(Usuario(14))