import random

def run():
    no_aleatorio = random.randint(1,101)
    no_elegido = int(input("Elije un numero entre el 1 y el 100, tienes 5 oportunidades:   "))
    vidas = 5
    if no_elegido <= 100:
        vidas -= 1
        while no_elegido != no_aleatorio and vidas >= 1:
            if no_elegido < no_aleatorio:
                print("¡Pista! Es un número mayor, te quedan "
                + str(vidas) + " oportunidades")
            else:
                print("¡Pista! Es un número menor, te quedan "
                + str(vidas) + " oportunidades")
            no_elegido = int(input("Elige otro número:   "))
            vidas -= 1

        if no_elegido == no_aleatorio:
            print("¡Felicidades! Adivinaste el número.")
        else:
            print("Lo siento mucho, perdiste. Vuelve a intentarlo.")
    else: 
        print("¡Ups! este numero no es un número correcto")

if __name__ == "__main__":
    run()