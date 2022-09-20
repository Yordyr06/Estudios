# -- COMENTARIOS EN PYTHON --

# Los comentarios en python son notas que estan desplegadas por
# todo el codigo con el fin de dejar notas o explicaciones de algun
# de codigo que merezca ser explicado o resaltado.

# Los comentarios se identifican porque inician con un: "#", lo que
# provoca esto es que el interprete de python ignorara todo lo que se
# encuentre a la izquiera del simbolo "#", si hay un "#" en mitad de
# una linea de codigo el interprete ejecutara el codigo hasta que 
# se tope con el "#". 

#"Esto es un comentario".
def example():
    if 5 > 3:
        print("5 es mayor que 3")
    else: #Aquí va otro comentario.
        print("no imprimas nada")

# Los comentarios son considerados buenas practicas en el mundo del
# desarrollo de software ya que como la mayor parte del tiempo estaremos
# leyendo código que otra persona programo siempre será util dejar
# explicaciones para el que vaya luego a leer el código