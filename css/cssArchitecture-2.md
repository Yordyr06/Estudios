# OOCSS, BEM, SMACSS, ITCSS y Atomic Design

Ahora que ya conoces qué implica trabajar con una [arquitectura de CSS][01], estudiemos las más comunes cuando se manipula código CSS.
[01]: https://platzi.com/clases/2467-frontend-developer/40846-que-son-las-arquitecturas-css-para-que-sirven/ "arquitectura de CSS"

## Qué es CSS orientado a objetos
La arquitectura OOCSS (Object Oriented CSS) consiste en separar la estructura principal y la piel o máscara.

En otras palabras, consiste en tener objetos que son estructuras principales. Estos objetos estarán unidos en una máscara, donde esta será la que cambie pero manteniendo la estructura intacta.

[![](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer34.png)](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer34.png)

## Qué es BEM: bloque, elemento y modificador
La arquitectura BEM (Block-Element-Modifier) es una de las más utilizadas actualmente. Consiste en manejar los elementos en clases definidas por bloques, elementos y modificadores.

    Bloque: es la estructura principal que es contenedora de varios elementos.
    Elemento: es el elemento HTML que hace referencia el contenedor.
    Modificador: es un estilo específico para el elemento. Por ejemplo, un botón que tenga un color diferente a los demás, esto tiene relación con la especificidad.

[![](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer35.png)](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer35.png)

Puedes revisar más sobre esta arquitectura en el siguiente artículo:
[    Guía de BEM para CSS | Cohete Falcon 9 de SpaceX][02]
[02]: https://platzi.com/blog/bem/ "    Guía de BEM para CSS | Cohete Falcon 9 de SpaceX"

## Qué es la arquitectura escalable y modular de CSS
La arquitectura SMACSS (Scalable and Modular Architecture for CSS) indica el orden de componentes que estarán ubicados en carpetas. La unión de estos componentes dará como resultado tu página web con estilos.

    Base: elementos base, como botones, títulos, enlaces.
    Layout: estructura de la página, relacionado con el Responsive Design.
    Módulos: elementos que contienen a los elementos base.
    Estado: estilos relacionados con el comportamiento de elemento, relacionado con las pseudoclases y pseudoelementos.
    Temas: conjunto de estilos que definen tu página web.

[![](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer36.png)](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer36.png)


## Qué es el triángulo invertido de CSS
La arquitectura ITCSS (Inverted Triangle CSS) consiste en separar los archivos del proyecto; mediante ajustes, herramientas, elementos, entre otros. Todo esto para manejar los detalles de especificidad, claridad y magnitud.

[![](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer37.png)](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer37.png)


## Qué es el diseño atómico
La arquitectura Atomic Design también es una de las más utilizadas actualmente. Consiste en manejar los elementos como una estructura mínima, a partir de la unión de varias de estas, dará como resultado los estilos de la página web. Se basa en la estructura mínima de la materia, los átomos.

    Átomos: estructura mínima; como botones, enlaces, títulos, entre otros.
    Moléculas: unión de átomos.
    Organismos: unión de moléculas.
    Plantillas: unión de organismos.
    Páginas: unión de plantillas.

[![](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer38.png)](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer38.png)

# LECTURAS RECOMENDADAS:
https://intelygenz.medium.com/how-to-organize-your-css-with-oocss-bem-smacss-a2317fa083a7
https://bradfrost.com/blog/post/atomic-web-design/
https://www.xfive.co/blog/itcss-scalable-maintainable-css-architecture/
https://medium.com/@GreenXIII/organize-your-css-smacss-way-89c087db5092
https://en.bem.info/methodology/
https://www.smashingmagazine.com/2011/12/an-introduction-to-object-oriented-css-oocss/#top
https://github.com/stubbornella/oocss/wiki
https://platzi.com/blog/bem/


# REFERENCIA:
[OOCSS, BEM, SMACSS, ITCSS y Atomic Design](https://platzi.com/clases/2467-frontend-developer/40847-oocss-bem-smacss-itcss-y-atomic-design/ "OOCSS, BEM, SMACSS, ITCSS y Atomic Design")