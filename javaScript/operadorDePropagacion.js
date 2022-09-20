// -- OPERADOR DE PROGACION --

// El operador de propagación (spread operator), como su nombre lo dice,
// consiste en propagar los elementos de un iterable, ya sea un array o stringm
// utilizando tres puntos (...) dentro de un array.

// Para strings
const array = [ ..."Hola"]    // [ 'H', 'o', 'l', 'a' ]

// En arrays
const otherArray = [ ...array]   //[ 'H', 'o', 'l', 'a' ]

// También se utiliza para objetos, pero esta característica fue añadida
// en versiones posteriores de ECMAScript y es denominada *Spread properties.

// Copiar arrays utilizando el operador de propagación
// Si quieres realizar una copia de una array, deberás tener cuidado de la
// referencia en memoria. Los arrays se guardan en una referencia en memoria,
// al crear una copia, la copia tendrá la misma referencia que el original,
// por lo que si cambias algo en la copia, también lo harás en el original.

const originalArray = [1,2,3,4,5]
const copyArray = originalArray
copyArray[0] = 0

originalArray // [0,2,3,4,5]
originalArray === copyArray  // true

// Para evitar esto, utiliza el operador de propagación para crear una
// copia del array que utilice una refencia en memoria diferente al original.

const originalArray = [1,2,3,4,5]
const copyArray = [...originalArray]
copyArray[0] = 0

originalArray // [1,2,3,4,5]
copyArray // [0,2,3,4,5]
originalArray === copyArray  // false

// Unir arrays y añadir elementos con el operador de propagación
// Para unir dos arrays con el operador de propagación, simplemente
// debes separarlos por comas en un array.

const array1 = [1,2,3]
const number = 4
const array2 = [5,6,7]

const otherArray = [ ...array1, number, ...array2 ]

otherArray // [1,2,3,4,5,6,7]

// Ten cuidado con la copia para diferentes niveles de profundidad
// El operador de propagación sirve para crear una copia en un solo
// nivel de profundidad, esto quiere decir que si existen objetos o
// arrays dentro del array a copiar. Entonces los sub elementos en cada
// nivel, tendrán la misma refencia en la copia y en el original.

const originalArray = [1, [2,3] ,4,5]
const copyArray = [...originalArray]

originalArray[1] === copyArray[1] // true

// La manera de solucionar es más compleja, tendrías que utilizar el
// operador de propagación para cada elemento en cada nivel de profundidad.

// Sin embargo, recientemente salió una forma de crear una copia profunda
// con StructuredClone, aunque es una característica muy reciente, así que
// revisa que navegadores tienen soporte.

const originalArray = [1, [2,3] ,4,5]
const copyArray = structuredClone(originalArray)

originalArray === copyArray  // false
originalArray[1] === copyArray[1] // false

