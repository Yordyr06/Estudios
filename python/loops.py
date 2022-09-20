# -- APRENDIENDO BUCLES --

# Un bucle es un ciclo continuo en todos los lenguajes de programación
# que nos permite iterar sobre nuestros pasos: magina un contador cíclico
# (1,2,3,4,5,6…) donde puedes agregar un paso más sobre tu programa principal.



# -- EJEMPLO DE BUCLE EN PYTHON --

# Para este ejemplo, utilizaremos las potencias hasta llegar a un número determinado:

def potencia(numero):
    potencia = 1

    while (potencia <= 10):
    
        result = numero ** potencia
        print('Potencia de {} elevado a la {} es {}'.format(numero, potencia, result))
        potencia += 1
        

def run():
    numero = int(input('Escribe el numero al cual quieres averiguarle la potencia: '))
    potencia(numero)


if __name__ == "__main__":
    run()