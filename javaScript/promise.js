// -- PROMESA --

// Una promesa es una forma de manejar el asincronismo en JavaScript.
// Si aún no sabes en qué consiste el asincronismo, no te preocupes,
// existe un curso completo de este tema.

// Solamente ten presente que la clase Promise y sus métodos then y catch
// fueron añadidos en ES6, por un problema del manejo del asincronismo con
// funciones desencadenantes, llamado Callback Hell{target="_blank"}.

const promesa = () => {
    return new Promise((resolve, reject) => {
        if(true) {
            resolve( "Se ha resuelto la promesa" )
        } else {
            reject( "Se ha rechazado la promesa" )
        }
    });
}

promesa
    .then( respuesta => console.log(respuesta) ) //En caso que se ejecute resolve
    .catch( error => console.log(error) ) //En caso que se ejecute reject