1️⃣ Responde las siguientes preguntas en la sección de comentarios:

    ¿Qué es una variable y para qué sirve?
        
        **Una variable es un espacio en memoria destinado a almacenar
        distintos tipos de información para luego utilizarlo.**

    ¿Cuál es la diferencia entre declarar e inicializar una variable?

        Declarar una variable hace referencia a unicamente su creacion,
        inicializarla es asignarle un valor que almacenar a dichovariable.
        https://platzi.com/blog/la-diferencia-entre-let-y-var/

    ¿Cuál es la diferencia entre sumar números y concatenar strings?

        Cuando se suman numeros se ocupa la operación matematica de sumar,
        por otro lado cuando se concatenan strings una palabra se adiera a la otra
        formando una suerte de "frase".

    ¿Cuál operador me permite sumar o concatenar?

        El operador suma (+)

2️⃣ Determina el nombre y tipo de dato para almacenar en variables la siguiente información:

    Nombre: STR
    Apellido: STR
    Nombre de usuario en Platzi: STR
    Edad: INT
    Correo electrónico: STR
    Mayor de edad: BOOL
    Dinero ahorrado: INT
    Deudas: INT

3️⃣ Traduce a código JavaScript las variables del ejemplo anterior y deja tu código en los comentarios:

    let nombre = "Yordy Leonardo";
    let apellido = "Almonte Ruiz";
    let usuarioPlatzi = "yordyr06";
    let edad = 26;
    let correoElectronico = "yoalmonte.dev@outlook.com";
    let mayorEdad = true;
    let ahorro = 500;
    let bill = -200000;

4️⃣ Calcula e imprime las siguientes variables a partir de las variables del ejemplo anterior:

    Nombre completo (nombre y apellido)

        let nombreCompleto = nombre + " " + apellido;
        console.log(nombreCompleto);

    Dinero real (dinero ahorrado menos deudas)

        let dineroReal = ahorro - bill;
        console.log(dineroAhorrado);

Funciones
1️⃣ Responde las siguientes preguntas en la sección de comentarios:

    ¿Qué es una función?

        Una función es un bloque de codigo que realiza una tarea
        especifica, que luego podra ser llamado en el momento que
        requeramos.

    ¿Cuándo me sirve usar una función en mi código?

        Las funciones son verdaderamente utiles cuando un bloque de
        codigo se repite deforma repetitiva, si volvemos una funcion
        el bloque de codigo que se repite varias veces esto nos permitira
        ahorrar lineas de codigo.

    ¿Cuál es la diferencia entre parámetros y argumentos de una función?

        Los parametros son las variables predetermnadas que una funcion puede requerir
        y que se especifican al momento de declarar una funcion y los argumentos son esas
        mismas variables pero ya con datos almacenados que pasaran a ser utilizados por 
        la funcion en especifico al momento de llamarla.


2️⃣ Convierte el siguiente código en una función, pero, cambiando cuando sea necesario las variables constantes por parámetros y argumentos en una función:

const name = "Juan David";
const lastname = "Castro Gallego";
const completeName = name + lastname;
const nickname = "juandc";

console.log("Mi nombre es " + completeName + ", pero prefiero que me digas " + nickname + ".");

Condicionales
1️⃣ Responde las siguientes preguntas en la sección de comentarios:

    ¿Qué es un condicional?
    ¿Qué tipos de condicionales existen en JavaScript y cuáles son sus diferencias?
    ¿Puedo combinar funciones y condicionales?

2️⃣ Replica el comportamiento del siguiente código que usa la sentencia switch utilizando if, else y else if:

const tipoDeSuscripcion = "Basic";

switch (tipoDeSuscripcion) {
   case "Free":
       console.log("Solo puedes tomar los cursos gratis");
       break;
   case "Basic":
       console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");
       break;
   case "Expert":
       console.log("Puedes tomar casi todos los cursos de Platzi durante un año");
       break;
   case "ExpertPlus":
       console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");
       break;
}

3️⃣ Replica el comportamiento de tu condicional anterior con if, else y else if, pero ahora solo con if (sin else ni else if).

    💡 Bonus: si ya eres una experta o experto en el lenguaje, te desafío a comentar cómo replicar este comportamiento con arrays u objetos y un solo condicional. 😏

Ciclos
1️⃣ Responde las siguientes preguntas en la sección de comentarios:

    ¿Qué es un ciclo?
    ¿Qué tipos de ciclos existen en JavaScript?
    ¿Qué es un ciclo infinito y por qué es un problema?
    ¿Puedo mezclar ciclos y condicionales?

2️⃣ Replica el comportamiento de los siguientes ciclos for utilizando ciclos while:

for (let i = 0; i < 5; i++) {
    console.log("El valor de i es: " + i);
}

for (let i = 10; i >= 2; i--) {
    console.log("El valor de i es: " + i);
}

3️⃣ Escribe un código en JavaScript que le pregunte a los usuarios cuánto es 2 + 2. Si responden bien, mostramos un mensaje de felicitaciones, pero si responden mal, volvemos a empezar.

    💡 Pista: puedes usar la función prompt de JavaScript.

Listas
1️⃣ Responde las siguientes preguntas en la sección de comentarios:

    ¿Qué es un array?
    ¿Qué es un objeto?
    ¿Cuándo es mejor usar objetos o arrays?
    ¿Puedo mezclar arrays con objetos o incluso objetos con arrays?

2️⃣ Crea una función que pueda recibir cualquier array como parámetro e imprima su primer elemento.
3️⃣ Crea una función que pueda recibir cualquier array como parámetro e imprima todos sus elementos uno por uno (no se vale imprimir el array completo).
4️⃣ Crea una función que pueda recibir cualquier objeto como parámetro e imprima todos sus elementos uno por uno (no se vale imprimir el objeto completo).