# -- QUÉ SON DICCIONARIOS EN PYTHON --

# Los diccionarios en Python son una estructura de datos mutable
# las cuales almacenan diferentes tipos de valores sin darle
# importancia a su orden. Identifican a cada elemento por una
# clave (Key). Se escriben entre {}.

mi_diccionario = {
    "key_1": "valor_1",
    "key_2": "valor_2",
    "key_3": "valor_3",
}

# -- METODOS Y COMANDOS BÁSICOS PARA DICCIONARIOS --

len(mi_diccionario) # Contara la cantidad de elementos que posea el diccionaro.
mi_diccionario["key_1"] # Retorna el elemento que contiene esta clave.
mi_diccionario["key_1"] = "nuevo_valor" # Reasigna el valor de una clave.
mi_diccionario["key_4"] = "nuevo_valor" # Agrega nuevos datos al diccionario.
mi_diccionario.get("key_1") # Otra forma de retorar el elemento que contiene esta clave
mi_diccionario.keys("valor") # Retorna la clave de nuestro elemento.
mi_diccionario.values() # Retorna una lista de elementos (valores del diccionario).
mi_diccionario.items() # Devuelve lista de tuplas (primero la clave y luego el valor).
mi_diccionario.clear() # Elimina todos los items del diccionario.
mi_diccionario.pop("key_1") # Elimina el elemento ingresado.
mi_diccionario.popitem() # Elimina el ultimo valor agredo.
del mi_diccionario["key_1"] # Es otra forma de elimina el elemento ingresado.
copia = mi_diccionario.copy() # genera una copia el diccionario indicado.
copia = dict(mi_diccionario) # Genera una copia del diccionario indicado.
mi_diccionario = dict(key_4 = "nuevo_valor") # Genera un diccionario o agrega nuevos valores a este.



# -- DICCIONARIOS ANIDADOS --

# Tambien es posible hacer un diccionariio que contenga más diccionarios
# dentro de si mismo, como tambien pueden contener tuplas y listas.
# Estos se codifican de la siguiente forma:

dicc_anidado = {
    "dicc_1": {
        "key_1": "valor_1",
        "key_2": "valor_1",
        "key_3": "valor_1",
    },
    "dicc_2": {
        "key_1": "valor_1",
        "key_2": "valor_1",
        "key_3": "valor_1",
    },
    "dicc_3": {
        "key_1": "valor_1",
        "key_2": "valor_1",
        "key_3": "valor_1",
    },
}

dicc_list = {
    "list_1": [1, 2, 3, 4, 5],
    "list_2": [10, 20, 30, 40, 50],
    "list_3": [100, 200, 300, 400, 500],
}

dicc_tuple = {
    "tuple_1": (1, 2, 3, 4, 5),
    "tuple_2": (10, 20, 30, 40, 50),
    "tuple_3": (100, 200, 300, 400, 500),
}