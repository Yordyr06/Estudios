# Tipos de selectores: pseudoclases y pseudoelementos

Existen otros tipos de selectores, además de los selectores básicos y combinadores, capaces de cambiar un estado o añadir algo más al elemento. Estos son denominados pseudoclases y pseudoelementos.

Cuáles son las pseudoclases

Una pseudoclase define el estilo de un estado especial de un elemento.

    Índice de pseudo-clases estándar.

Sintaxis

selector : pseudoclase { 
    propiedad: valor;
}

:hover

Representa el estado en el cual el cursor está encima del elemento.

    Ejemplo

:active

Representa el estado de un elemento que no ha sido visitado.

    Ejemplo

:visited

Representa el estado de un elemento que ya ha sido visitado.

    Ejemplo

:not()

Representa el estado en el cual no coinciden los selectores que se indiquen.

    Ejemplo

:nth-child()

Representa el estado en el cual coinciden los hijos del elemento según el valor indicado.

Valores de palabras clave:

    odd: los elementos hijos en posiciones impares.
    even: los elementos hijos en posiciones pares.

Fórmula matemática: An+B donde A y B son números enteros.

    Ejemplo

Cuáles son los pseudoselementos

Un pseudoelemento define el estilo de una parte específica de un elemento.

    Lista de pseudo-elementos.

Sintaxis

selector :: pseudo-elemento { 
    propiedad: valor;
}

::before

Sirve para agregar un contenido antes del elemento. El contenido es agregado mediante la propiedad content de CSS.

    Ejemplo

::after

Sirve para agregar un contenido después del elemento. El contenido es agregado mediante la propiedad content de CSS.

    Ejemplo

::first-letter

Sirve para añadir estilos a a la primera letra del texto de cualquier elemento.

    Ejemplo


# Lecturas recomendadas

https://github.com/platzi/curso-frontend-developer/blob/5108689bdb6599cc92bd9595db28784f9be48704/curso-1/selectores-3.html
https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements
https://css-tricks.com/pseudo-class-selectors/