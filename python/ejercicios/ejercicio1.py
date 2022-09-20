a = int(input("Ingrese un numero: "))
b = int(input("ingrese un segundo numero que multiplicara el primero: "))
c = 0

for x in range(b):
    c += a

print("El resultado es: {}".format(c))