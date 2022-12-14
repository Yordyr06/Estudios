// -- Funciones en Flecha (Arrow Functions) --

// Las funciones flecha (arrow functions) consiste en
// una función anónima con la siguiente estructura:


//Función tradicional (ECMASCript 5)
function nombre (parámetros) {
    return (valorRetornado)
}

//Función flecha (ECMASCript 6 en adelante)
const nombre = (parámetros) => {
    return (valorRetornado)
}

// Se denominan función flecha por el elemento => en su sintaxis.
// Si existe un solo parámetro, puedes omitir los paréntesis.

const porDos = num => num * 2



// -- Retorno implícito --

// Las funciones flecha tienen un retorno implícito, es decir,
// se puede omitir la palabra reservada return, y que el código
// sea escrito en una sola línea.

// Si el retorno requiere de más líneas y aún deseas utilizarlo
// de manera implícita, deberás envolver la instrucción entre paréntesis.

//Función tradicional
function suma (num1, num2) {
    return num1 + num2
}

//Función flecha
const resta = (num1, num2) => num1 - num2
const suma = (num1, num2) => (
    num1 + num2
)