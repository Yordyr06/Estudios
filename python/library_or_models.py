#  -- MODULOS O LIBRERIAS --

# Los modulos o librerias pueden considerarse como un paquete de instrucciones,
# funciones y/o variables prediseñados para resolver problemas en especifico que
# podremos incluir en nuestros archivos a la hora de programar. Estos los podemos
# crear nosotros mismos o descargarlos desde internet, de esta forma nosotros podemos
# reutilizar el código de otros colegas y/o nuestro propio código, es una buena
# practica utilizar las librerias necesarias (pero sin exagerar) ya que así mantenmos
# el codigo eficiente y ordenado permitiendonos programar más y escribir menos.

# Este concepto es bastante poderoso en programación y está disponible en otros
# leguajes de programación por ejemplo: Java, JavaScript, Ruby, Python (obviamente),
# entre otros más. El uso de librerias fomenta el trabajo en equipo y el pensamiento
# de no reinventar la rueda, si alguien ya ideo una forma eficiente de resolver un
# problema tomemos eso para resolver nuestro propio problema o en el minimo de los
# casos cubrir una buena parte del problema.

# Como se mencionó anteriormente, las librerias es un concepto muy podereroso con el
# que podremos importar por ejemplo: clases de usuario con metodos como iniciar sesión,
# abrir sesión, cambiar datos, egistro de usuario y un grandisimo etc, por esta razón es
# muy importante conocer el potencial de las librerias en el mundo de la programación.




#  -- CREANDO Y DESCARGANDO LIBRERIAS --

# Para crear una libreria primero debemos crear el archivo que hará la función de libreria
# y luego exportarlo con la instruccion "import" al archivo que deseamos exportar, seguida
# del nombre de la libreria. Por otro apareceran momentos enlos que solo necesitamos algo
# puntual de una libreria, en ese caso utilizamos la instruccion "from", colacamos el
# nombre de la libreria y luego con la instrucción "import" pasaremos a detallar la parte
# exacta que necesitamos como por ejemplo el nombre de una funcion.

# Importando librerias con "import", cuando empleamos esta debemos especificar que queremos
# utilizar de la libreria ej: <nombre_libreria>.<nombre_funcion>
import indentation
indentation.example

# Importando una parte de una librerias, de esta forma solo debemos invocar lo importado ya que
# se especifico que se necesita y dedonde, ej: <funcion()>
from comentaries import example
example()

# A las librerias se le pueden asignar otro nombre con la instrucción as despues de indicar la
# libreria
import math as x
print(x.sqrt(9))



#  -- DESCARGANDO E INSTALANDO LIBRERIAS  DE PYTHON --

# Para adquirir modulos o librerias de python se debe de comprender de forma básica la linea
# de comandos del sisitema que se este ulitizando. Grancias a la herramienta pip es posible
# gestionar la descarga e instalacion de modulos o librerias a base de comandos en una terminal,
# la herramienta pip descarga las librerias desde la pagina https://pypi.org/ que es la pagina
# oficial de las librerias del lenguaje python.

# Por lo general cada libreria es responsable de su porpia documentacion por lo tanto no todas tendran
# una documentación clara y consiza con todas las instrucciones posibles ycada una es independiente
# des las otras a menos de que exista un proyecto en conjunto.


# -- COMANDOS BÁSICOS DE PIP --

# $ pip install <nombre_libreria>: por logeneral es la forma en que se descargan y se instalan librerias.
# $ pip unistall <nombre_libreria>: por lo general es la forma en que se desintalan y se borran librerias.
# $ pip list: despliega una lista de todas las librerias instaladas.
# $ python -m pip install --upgrade pip: muestra el listado de actualizaciones pendientes.