miLista = []

print("""
    Ingrese cuantos valores quiera para sumarlos,
    cuando ya sean suficiente escriba: "basta".
    """)

while True:
    valor = input("Ingrese un valor: ")
    if valor == "basta":
        break
    else:
        try:
            valor = float(valor)
            miLista.append(valor)
        except:
            print("Valor invalido, ingrese un valor correcto.")

resultado = 0
for x in miLista:
    resultado += x

print("El resultado de la suma de todos los valores ingresados es {}." .format(resultado))