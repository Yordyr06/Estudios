-- GIT REBASE: REORGANIZANDO EL TRABAJO REALIZADO --

Rebase es el proceso de mover o combinar una secuencia de confirmaciones
en una nueva confirmación base. La reorganización es muy útil y se visualiza
fácilmente en el contexto de un flujo de trabajo de ramas de funciones.

Para hacer un rebase de una rama a otra, correrías los
siguientes comandos:

* git checkout nombre_primera_rama
* git rebase nombre_segunda_rama
# No reorganices el historial público

Nunca debes reorganizar las confirmaciones una vez que se hayan enviado a un
repositorio público. La reorganización sustituiría las confirmaciones antiguas
por las nuevas y parecería que esa parte del historial de tu proyecto se hubiera
desvanecido de repente.

El comando rebase es **_una mala práctica, sobre todo en repositorios remotos.
Se debe evitar su uso, pero para efectos de práctica te lo vamos a mostrar,
para que hagas tus propios experimentos. Con rebase puedes recoger todos los
cambios confirmados en una rama y ponerlos sobre otra.

# Cambiamos a la rama que queremos traer los cambios
* git checkout experiment
# Aplicamos rebase para traer los cambios de la rama que queremos 
* git rebase master