def guardarNombreYApellido():
    print("""
        Los nombres y apellidos que ingreses serán guardados
        en un archivo de texto que hará la función de base
        de datos para fines practicos.
        """)

    nombre = input("Ingresa tu nombre o tus nombres: ")
    apellido = input("Ingresa tus apellidos: ")
    txt = open("nombres_y_apellidos.txt", "a")
    txt.write(nombre + " " + apellido + "\n")
    txt.close()

guardarNombreYApellido()