word = input("Escribe una palabra: ")
vocales = 0

for x in word:
    y = x.lower()
    if y == "a" or y == "e" or y == "i" or y == "o" or y == "u":
        vocales += 1
    else:
        volaces = 0

print("Esta palabra tiene {} vocales".format(vocales))