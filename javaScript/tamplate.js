// -- ¿QUÉ SON PLANTILLAS LITERALES? --

// Las plantillas literales (template literals) consisten en crear
// cadenas de caracteres que puedan contener variables.

// Antes de ES6, si querías crear una cadena larga o un mensaje,
// debías utilizar la concatenación.

function newFunction(name, age, country) {
    var name = name || 'oscar';
    var age = age || 32;
    var country = country || 'MX';
    console.log(name, age, country);
  }
  
  // es6
  function newFunction2(name = 'oscar', age = 32, country = "MX") {
    console.log(name, age, country);
  };
  
  newFunction2();
  newFunction2('Ricardo', '23', 'CO');

// //Esto trae varios problemas en la legibilidad y mantenibilidad del código.
// Se convierte cada vez más complejo en mensajes más extensos o el estar
// pendiente de agregar espacios antes o después de cada variable concatenada.

// //Con las plantillas literales añadidas en ES6, emplea el caracter ( ` ),
// que no es una comilla simple ( ’ ), para envolver el mensaje e incluir las
// variables con la sintaxis ${variable}.   

// De esta manera el código es más legible y que pueda mantenerse.

  let hello = "Hello";
  let world = "World";
  let epicPhrase = hello + ' ' + world;
  console.log(epicPhrase);
  let epicPhrase2 = `${hello} ${world}`;
  console.log(epicPhrase2);
  
  let lorem = "Qui consequatur. Commodi. Ipsum vel duis yet minima \n"
    + "otra frase epica que necesitamos."
  
  // es6
  let lorem2 = `otra frase epica que necesitamos
  ahora es otra frase epica
  `;
  
  console.log(lorem);
  console.log(lorem2);
  
  let person = {
    'name': 'oscar',
    'age': 32,
    'country': 'MX'
  }
  
  console.log(person.name, person.age);
  
  let { name } = person;
  console.log(name);
  
  let team1 = ['Oscar', 'Julian', 'Ricardo'];
  let team2 = ['Valeria', 'Yesica', 'Camila'];
  
  let education = ['David', ...team1, ...team2];
  
  console.log(education);
  
  {
    var globalVar = "Global Var";
  }
  
  {
    let globalLet = 'Global Let';
    console.log(globalLet);
  }
  
  console.log(globalVar);
  
  const a = 'b';
  a = 'a';
  console.log(a);