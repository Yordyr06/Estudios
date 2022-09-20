# Posicionamiento en CSS

El posicionamiento en CSS consiste en cómo un elemento se situará, con respecto a su elemento padre y al flujo normal del documento. El flujo normal del documento es el orden de los elementos establecidos en el HTML.

La posición del elemento se la define con la propiedad position, mediante los siguientes valores:

    static
    relative
    absolute
    sticky

Propiedades de posición

Además de la propiedad position, existen cuatro propiedades del elemento de acuerdo a su posición con respecto a su padre, estas son: top (arriba), bottom (debajo), left (izquierda) y right (derecha).

div {
    top: 10px;
    bottom: 15px;
    left: 20px;
    right: 10px;
}

Estos valores estarán establecidos en el padre próximo que tenga la posición relative.

Si top y bottom están definidos, top gana. Si left y rigth están definidos, left gana (dependiendo el idioma configurado).
Posición estática

La posición static es el valor por defecto de todo elemento HTML, consiste en respetar el flujo normal del documento donde las propiedades de posición no pueden ser establecidas.

    Ejemplo position static

Posición relative

La posición relative consiste en respetar el flujo normal del documento donde las propiedades de posición sí pueden ser establecidas.

    Ejemplo position relative

Posición absoluta

La posición absolute consiste en quitar al elemento del flujo normal del documento donde las propiedades de posición sí pueden ser establecidas.

En el siguiente ejemplo, observa que pasa con el primer elemento con respecto a los demás.

    Ejemplo position absolute

Habrás notado que el elemento “2” desaparece, pero en realidad lo que sucede es que sitúa por detrás del elemento con posición absoluta que salió del flujo normal del documento. Este comportamiento se debe al eje Z de la pantalla y al contexto de apilamiento.
Elemento padre más próximo con posición relativa

El elemento con posición absoluta se desplazará arriba, abajo, izquierda o derecha con respecto al elemento padre más próximo con posición relativa.

Si no existe un padre con posición relativa de un elemento con posición absoluta, este se desplazará con respecto al elemento raíz del documento.

En el siguiente ejemplo, te encontrarás varios contenedores padres, incluso las etiquetas <html> y <body>. Sigue los pasos y observa el comportamiento. Ignora los estilos iniciales, simplemente sirven para establecer la estructura del ejercicio.

    Ejemplo de position en diferentes contenedores padre

Como pudiste observar, en el elemento con posición absoluta, su desplazamiento se basa con relación al elemento padre más próximo con posición relativa.
Posición fija

La posición fixed consiste en quitar al elemento del flujo normal del documento y fijarlo en un lugar; donde las propiedades de posición sí pueden ser establecidas.

En el siguiente ejemplo, desplázate por el documento, observa el comportamiento antes y después de colocar la posición fija.

    Ejemplo position fixed

Posición variable fija

La posición sticky consiste en quitar al elemento del flujo normal del documento y fijarlo en un lugar mientras su contenedor sea visible; donde las propiedades de posición sí pueden ser establecidas.

En el siguiente ejemplo, desplázate por el documento, observa el comportamiento antes y después de colocar la posición variable fija.

    Ejemplo de position sticky


# LECTURAS RECOMENDADAS:

https://github.com/platzi/curso-frontend-developer/blob/5108689bdb6599cc92bd9595db28784f9be48704/curso-1/posicionamiento.html