// -- ¿QUÉ SON LOS PARAMETROS EN OBJETOS? --

// Los parámetros en objetos son una función que consiste en crear
// objetos a partir de variables sin repetir su nombre como propiedad.

// Antes de ES6, para crear un objeto a partir de variables consistía
// de la siguiente manera:

const nombre = "Andres"
const edad = 23

const objeto = {
    nombre: nombre, 
    edad: edad
 }

objeto // { nombre: 'Andres', edad: 23 }

// Con los parámetros en objetos puedes obviar la repetición de nombres,
// JavaScript creará la propiedad a partir del nombre de la variable con
// su respectivo valor.

const name = "Andres"
const age = 23

const object = {nombre, edad}

objeto // { nombre: 'Andres', edad: 23 }

// El resultado es el mismo, pero sin la necesidad de repetir palabras.