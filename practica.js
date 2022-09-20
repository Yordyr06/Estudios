// 3️⃣ Traduce a código JavaScript las variables del ejemplo anterior
// y deja tu código en los comentarios:
let nombre = "Yordy Leonardo";
let apellido = "Almonte Ruiz";
let usuarioPlatzi = "yord";
let edad = 26;
let correoElectronico = "yoalmonte.dev@outlook.com";
let mayorEdad = true;
let ahorro = 500;
let bill = 200000;



//4️⃣ Calcula e imprime las siguientes variables a partir de las variables del ejemplo anterior:

// Nombre completo (nombre y apellido)
let nombreCompleto = nombre + " " + apellido;
console.log(nombreCompleto);

// Dinero real (dinero ahorrado menos deudas)
let dineroReal = ahorro - bill;
console.log(dineroAhorrado);




//2️⃣ Convierte el siguiente código en una función, pero, cambiando cuando
// sea necesario las variables constantes por parámetros y argumentos en una función:

// const name = "Juan David";
// const lastname = "Castro Gallego";
// const completeName = name + lastname;
// const nickname = "juandc";

// console.log("Mi nombre es " + completeName + ", pero prefiero que me digas " + nickname + ".");

function myName(name, lastName, nickname) {
    const completeName = name + " " +lastName;
    console.log("Mi nombres es " + completeName + ", pero prefiero que me llames " + nickname + ".");
}



// 2️⃣ Replica el comportamiento del siguiente código que usa la sentencia switch utilizando if, else y else if:

const tipoDeSuscripcion = "Basic";

// switch (tipoDeSuscripcion) {
//    case "Free":
//        console.log("Solo puedes tomar los cursos gratis");
//        break;
//    case "Basic":
//        console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");
//        break;
//    case "Expert":
//        console.log("Puedes tomar casi todos los cursos de Platzi durante un año");
//        break;
//    case "ExpertPlus":
//        console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");
//        break;
// }

if (tipoDeSuscripcion == "Basic") {
    console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");
}
else if (tipoDeSuscripcion == "Expert") {
    console.log("Puedes tomar casi todos los cursos de Platzi durante un año");
}
else if (tipoDeSuscripcion == "ExpertPlus") {
    console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");
}
else {
    console.log("Solo puedes tomar los cursos gratis de Platzi");
}