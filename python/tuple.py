# -- ENTENDIENDO COMO FUNCIONAN LAS TUPLAS --

# Las tuplas son estructuras de datos inmutables. Es decir, no puedes
# modificar una tupla a agregando o quitando un valor. Lo único que puedes
# hacer es definir de nuevo esa tupla a. Los objetos inmutables (como los strings)
# son tipos de datos para Python que apuntan a un lugar específico en memoria
# y que su contenido no puede ser cambiado. Al cambiar el contenido predefiniendo
# el contenido de la variable a, entonces cambiará su posición en memoria.



# -- COMANDOS BÁSICOS PARA TRABAJAR CON TUPLAS EN PYTHON --

#     * Declarar tupla
mi_tupla = ()
mi_tupla = (1,2,3)

#     * Generar una tupla de 1 solo valor (la , es obligatoria.)
mi_tupla = (1,)

#     * Acceder a un índice de la tupla
mi_tupla = (1,2,3)
mi_tupla[0] #1
mi_tupla[1] #2
mi_tupla[2] #3

#     * Reasignar una tupla
mi_tupla = (1,2,3)
mi_otra_tupla = (4,5,6)
mi_tupla =+ mi_otra_tupla



# -- MÉTODOS BÁSIDOS PARA TRABAJAR CON TUPLAS --
    
nombre_tupla.count("Elemento") # Cuenta las veces que esta un elemento en lista
nombre_tupla.index("Elemento") # Indica el indice de un elemento especifico. 
list(nombre_tupla) # Convierte una tupla en una lista.