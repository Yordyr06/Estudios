def conversor(divisa, valor_usd, valor_eur, valor_btc, valor_eth):
    moneda = float(input("¿Cuantos pesos " + divisa + " tiene?  "))
    usd = moneda / valor_usd
    usd = round(usd, 2)
    usd = str(usd)
    eur = moneda / valor_eur
    eur = round(eur, 2)
    eur = str(eur)
    btc = moneda / valor_btc
    btc = round(btc, 8)
    btc = str(btc)
    eth = moneda / valor_eth
    eth = round(eth, 8)
    eth = str(eth)
    print("Tiene un total de $" + usd + " dolares")
    print("Tiene un total de €" + eur + " euros")
    print("Tiene un total de " + btc + " bitcoins")
    print("Tiene un total de " + eth + " ethereums")


def main():
    menu = """
    Bienvenido al conversor de divisas:

    1: Peso dominicano
    2: Peso mexicano
    3: Peso argentino
    4: Peso cubano
    5: Peso uruguayo

    Elige una opción:   """
    # De derecha a izquierda: llamo a la funcion input, le paso la variable "menu" para que la
    # imprima y reciba el número que el usuario escogió, lo convierto a int y lo guardo en la
    # variable "opcion"
    option = int(input(menu))

    if option == 1:
        conversor("dominicanos", 54.14, 55.30, 1224085.02, 124542.38)
    
    elif option == 2:
        conversor("mexicanos", 20.46, 20.92, 449825.62, 30903.96)
    
    elif option == 3:
        conversor("argentino", 130.39, 133.27, 2866814.96, 196958.00)

    elif option == 4:
        conversor("cubano", 23.99, 24.52, 524742.84, 35880.36)
    
    elif option == 5:
        conversor("uruguayo", 41.80, 42.73, 913580.30, 62496.11)
   
    else:
        print("Elige una opción correcta")


if __name__ == "__main__":
    main()