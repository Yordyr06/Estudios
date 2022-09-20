// -- VARIABLES EN JAVASCRIPT --

// Dentro de JavaScript tenemos tres formas de declarar una
// variable las cuales son: var, const y let.



// -- VAR --

// Era la forma en que se declaraban las variables hasta
// ECMAScript 5. Casi ya no se usa porque es de forma global y
// tiene las siguientes características:

//     * Se puede reinicializar: osea todas las variables se inicializan, por ejemplo:
//         Var pokemonType = ‘electric’ entonces reinicializar es:
//         Var pokemonType = ‘grass’ osea la misma variable con diferentes datos el
//             último dato predomina.
    
//     * Se puede reasignar: osea la variable ya inicializada le reasignamos otro valor
//         por ejemplo: inicializamos la variable: Var pokemonType = ‘electric’ ahora
//         la reasignamos pokemonType = ‘grass’ ya no va var
    
//     * Su alcance es función global: osea inicializamos la variable, pero la podemos
//         llamar desde cualquier bloque (una llave abierta y una cerrada {})
//         pero hay que tener mucho cuidado con ello ya que puede haber peligro,
//         no es recomendable usar VAR.



// -- CONST Y LET --

// Es la forma en que se declaran las variables a partir de ECMAScript 6.

// CONST: sirve para declarar variables que nunca van a ser modificadas:

//     * No se puede reinicilizar: es una const única no puede haber otra inicializada
//     con el mismo nombre.
            
//          - const pokemonType = ‘electric’ no puede haber: const pokemonType = ‘grass’

//     * No se pude reasignar: una vez que la hayamos inicializado no la podemos
//     reasignar solo con su nombre: 
        
//         - const pokemonType = ‘electric’
//         - no puede ejecutarse: pokemonType = ‘grass’ No es inmutable

// LET: Son variables que pueden ser modificadas, se pueden cambiar:
        
//     * No se puede reinicilizar: es una const única no puede haber otra inicializada
//     con el mismo nombre.
        
//         - let pokemonType = ‘electric’ 
//         - no puede haber: let pokemonType = ‘grass’

//     * Se puede reasignar: Osea la variable ya inicializada le reasignamos otro valor
//     por ejemplo, inicializamos la variable:
        
//         - let pokemonType = ‘electric’ ahora la reasignamos pokemonType = ‘grass’
        
//     * Su contexto de es bloque: Solo funciona dentro de un bloque {}, fuera de ello no.
