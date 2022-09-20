// -- LETS Y CONTS, LA NUEVA FORMA DE DECLARAR VARIABLES --

// Hasta ahora aprendiste a declarar variables con var, sin embargo,
// a partir de la especificación de ES6 se agregaron nuevas formas para
// la declaración de variables.

// Let y const resuelven varios problemas con var como el hoisting,
// variables globales, re-declaración y re-asignación de variables.



// -- SCOPE --
// En el tema del scope, se diferencian porque let y const tienen un
// scope de bloque y var no.

{
    var nameVar = "soy var"
    let nameLet = "soy let"
}    
    
    console.log(nameVar) // 'soy var'
    console.log(nameLet) // ReferenceError: nameLet is not defined



// -- OBJETO GLOBAL --
// En variables globales, let y constno guardan sus variables en el objeto
// global (window, global o globalThis), mientras que var si lo guarda.

{
    var nameVar = "soy var"
    let nameLet = "soy let"
    const nameConst = "soy const"
}
    globalThis.nameVar   // 'soy var'
    globalThis.nameLet   // undefined
    globalThis.nameConst  // undefined



// -- VARIABLES RE-DECLARADAS Y RE-ASIGNADAS

// La re-declaración es volver a declarar una variable, y la re-asignación
// es volver a asignar un valor, entonces cada variable tiene una forma diferente
// de manejarlas:

    // Una variable declarada con var puede ser re-declarada y re-asignada.
    // Una variable declarada con let puede ser re-asignada, pero no re-declarada.
    // Una variable declarada con const no puede ser re-declarada, ni re-asignada.
    // Su declaración y asignación debe ser en una línea, caso contrario habrá un error.

// En conclusión, si intentas re-declarar una variable declarada con let y const
// habrá un error de “variable ya declarada”; y, si intentas re-asignar una variable
// declarada con const existirá un error de tipo.

// En los demás casos, JavaScript lo aceptará como válidos, algo problemático con var,
//por eso deja de utilizarlo.

// Declarar y asignar con const
const pi = 3.14  // SyntaxError: Missing initializer in const declaration.

// Declaración de variables
{
    var nameVar = "soy var"
    let nameLet = "soy let"
    const nameConst = "soy const"
}
// Re-declaración de variables
var nameVar = "var soy" 
console.log(nameVar) // 'var soy'

let nameLet = "let soy" // SyntaxError: Identifier 'nameLet' has already been declared.

const nameConst = "const soy" //SyntaxError: Identifier 'nameConst' has already been declared.

// Re-asignación de variables
nameVar = "otro var"
console.log(nameVar) // 'otro var'

nameLet = "otro let"
console.log(nameVar) // otro let'

nameConst = "otro const" //TypeError: Assignment to constant variable.
