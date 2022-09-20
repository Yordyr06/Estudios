// -- PLANTILLA MULTILINEA--

//La plantilla multilínea consiste en crear mensajes que
//contengan varias líneas separadas entre sí, utilizando las
//plantillas literales: https://platzi.com/clases/1815-ecmascript-6/26121-default-params-y-concatenacion/

//Antes de ES6, la forma de crear una plantilla multilínea era agregar \n al string.

var mensaje = "Línea 1 \n" + "línea 2"

console.log(mensaje)
// 'Línea 1
// línea 2'

// Con ES6 solamente necesitas utilizar las plantillas literales.

const mensaje = `Línea 1
línea 2`

console.log(mensaje)
// 'Línea 1
// línea 2'



// -- DESESTRUCTURACIÓN--

// //La desestructuración (destructuring) consiste en extraer los valores
// de arrays o propiedades de objetos en distintas variables.

//     Desestructuración de objetos
//     La desestructuración de objetos consiste en extraer las propiedades
//     de un objeto en variables, utilizando el mismo nombre de la propiedad
//     en el objeto con la siguiente sintaxis:

const objeto = { prop1: "valor1", prop2: "valor2"}

// Desestructuración
const { prop1, prop2 } = objeto

// Antes de ES6, necesitabas acceder al objeto con la notación punto o corchetes
// por cada propiedad que se necesita y asignar ese valor a una variable diferente.

var usuario = { nombre: "Andres", edad: 23, plataforma: "Platzi" }

var nombre = usuario.nombre
var edad = usuario.edad
var plataforma = usuario["plataforma"]

console.log(nombre)  // 'Andres' 
console.log(edad)  // 23
console.log(plataforma)  // 'Platzi'

//Con la desestructuración puedes realizar lo mismo, pero en una sola
//línea, provocando que el código seas más legible y mantenible.

const usuario = { nombre: "Andres", edad: 23, plataforma: "Platzi" }

const { nombre, edad, plataforma } = usuario

console.log(nombre)  // 'Andres' 
console.log(edad)  // 23
console.log(plataforma)  // 'Platzi'

//Cambiar el nombre de las variables con desestructuración
//Si no te agrada el nombre de la propiedad del objeto, puedes
//cambiarlo utilizando la siguiente sintaxis:

const objeto = { prop1: "valor1", prop2: "valor2"}

// Desestructuración
const { prop1: newProp1, prop2: newProp2 } = objeto

//Por ejemplo:

const usuario = { nombre: "Andres", edad: 23, plataforma: "Platzi" }

const { nombre: name, edad: age, plataforma: platform } = usuario

console.log(name)  // 'Andres' 
console.log(age)  // 23
console.log(platform)  // 'Platzi'

console.log(nombre)   // Uncaught ReferenceError: nombre is not defined

// Desestructuración en parámetros de una función
// Si envías un objeto como argumento en la invocación a la declaración de
// una función, puedes utilizar la desestructuración en los parámetros para
// obtener los valores directamente. Ten en cuenta que el nombre debe ser igual
// a la propiedad del objeto.

const usuario = { nombre: "Andres", edad: 23, plataforma: "Platzi" }

function mostrarDatos( { nombre, edad, plataforma } ){
    console.log(nombre, edad, plataforma) 
}

mostrarDatos(usuario) // 'Andres', 23, 'Platzi'

// Desestructuración de arrays
// La desestructuración de objetos consiste en extraer los valores de un objeto
// en variables, utilizando la misma posición del array con una sintaxis similar
// a la desestructuración de objetos.

const array = [ 1, 2, 3, 4, 5 ]

// Desestructuración
const [uno, dos, tres ] = array

console.log(uno) // 1
console.log(dos) // 2
console.log(tres) // 3

// Desestructuración para valores retornados de una función
// Cuando una función retorna un array, puedes guardarlo en una variable por medio
// de la invocación. Por ende, puedes utilizar la desestructuración para utilizar esos
// valores por separado de manera legible.

// En el siguiente ejemplo, la función useState retorna un array con dos elementos:
// un valor y otra función actualizadora.

function useState(value){
    return [value, updateValue()]
}

//Sin desestructuración 
const
    estado = useState(3)
    valor = estado[0]
    actualizador = estado[1]

//Con desestructuración 
const [valor, actualizador] = useState(3)

// Lo que puedes hacer con desestructuración, pero no es recomendable

// Si necesitas un elemento en cierta posición, puedes utilizar la 
// eparación por comas para identificar la variable que necesitas.

const array = [ 1, 2, 3, 4, 5 ]

const [ ,,,,  cinco ] = array

console.log(cinco) // 5

// Como los arrays son un tipo de objeto, puedes utilizar la desestructuración
// de objetos mediante el índice y utilizando un nombre para la variable.

const array = [ 1, 2, 3, 4, 5 ]

const {4: cinco} = array

console.log(cinco) // 5
