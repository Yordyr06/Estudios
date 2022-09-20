# -- ALMACENANDO VARIOS VALORES EN UNA VARIABLE --

# Las listas nos permiten guardar múltiples valores en una sola variable.
# Estas listas en Python nos permiten guardar elementos del mismo tipo o
# diferentes, por lo que podemos tener strings, números enteros y decimales
# juntos en una misma variable. Las listas también son conocidas como arrays
# en otros lenguajes programación.



# -- COMANDOS BÁSICOS PARA TRABAJAR CON LISTAS EN PYTHON --

#     * Declarar lista
my_lista = []

#     * Unir listas
my_lista = [1]
my_lista2 = [2,3,4]
my_lista3 = my_lista + my_lista2
my_lista3 # [1,2,3,4]

#     * Partir listas como slices
my_lista = [1,2,3]
my_lista[1:] # [2,3]

#     * Extender una lista
my_lista = [1]
my_lista2 = [2,3,4]
my_lista.extend(my_lista2) # [1,2,3,4]

#     * Multiplicar listas
my_lista = ['a']
my_lista2 = my_lista * 5
my_lista2 # ['a','a','a','a','a']

#     * Eliminar el último elemento de la lista
my_lista = [1,2,3,4,5]
my_lista = my_lista.pop()
my_lista # [1,2,3,4]

#     * Ordenar lista
my_lista = [2,1,5,4,3]
my_lista = my_lista.sort()
my_lista # [1,2,3,4,5]

#     * Eliminar un elemento
my_lista = [1,2,3,4,5]
del my_lista[0]
my_lista # [2,3,4,5]

#     * Eliminar si conocemos su valor
my_lista = [1,2,3,4,5]
my_lista.remove(3)
my_lista # [1,2,4,5]

#     * saber qué métodos hay dentro de un elemento
my_lista = [1,2,3,4,5]
dir(my_lista) # ['__add__', '__class__', '__contains__', ...]

#     * Modificar un elemento
my_lista = [1,2,3,4,5]
my_lista[0] = 100
my_lista # [100,2,3,4,5]

#      * Añadir un elemento al final
my_lista = [1,2,3,4,5]
my_lista.append(6)
my_lista # [1,2,3,4,5,6]

#     * Organizar una lista (debe de contener los mismos tipos de datos)
my_lista = [2,5,1,3,4]
my_lista.sort() #[1,2,3,4,5]



# -- MÉTODOS BÁSICOS ADICIONALES PARA LAS LISTAS -- 

my_lista.sorted() # También ordena como sort() pero modifica la lista inicial
my_lista.clear() # Vacía la lista
my_lista.count() #  Cuenta las veces que esta un elemento en lista
my_lista.index() # Indica la posición donde esta un elemento de la lista
my_lista.insert() # Inserta un elemento en una posición dada ej: lista.insert(posición,item)
my_lista.reverse() # Le da la vuelta a una lista