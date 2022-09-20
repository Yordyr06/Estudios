# Modelo de caja

El modelo de caja se compone de cuatro elementos: margin, border, padding y contenido.

Si entras a las herramientas de desarrollador de tu navegador y señalas un elemento HTML, en la sección de estilos te aparecerá una vista parecida a la anterior imagen, este es el modelo de caja del elemento señalado.
Qué es el contenido del elemento HTML

El contenido del elemento, como su nombre lo indica, es todo lo que está dentro del elemento. Este tiene medidas establecidas por las propiedades width y height, que representan la anchura y la altura, respectivamente. Si imaginamos una caja, este valor sería todo lo que decidas colocar dentro.

div {
    width: 100px;
    height: 100px;
}

Qué son los bordes del elemento HTML

El border consiste en el perfil o borde de un elemento HTML. Si imaginamos una caja, sería la caja en sí. Para definir un borde es necesario utilizar las siguientes tres propiedades:

    border-color: establece el color del borde.
    border-style: establece el estilo propio del borde, estos pueden ser: none (sin borde), dotted (puntos), dashed (guiones), solid (continuo), double (doble continuo), groove (recuadro).
    border-width: estable la anchura del borde.

También se puede establecer los tres valores en una sola propiedad border donde no importa el orden.

div {
    border: [color] [style] [width];
}

div {
    border-color: red;
    border-style: solid;
    border-width: 1px;
}

    Ejemplo de bordes

También estableciendo de manera individual los valores de cada posición:

div {
  border-top: 5px solid blue;
  border-bottom: 5px solid red;
  border-left: 5px solid black;
  border-right: 5px solid yellow;
}

Qué es el espaciado interno del elemento HTML o padding

El padding consiste en el espacio entre el borde y el contenido del elemento HTML. Si imaginamos una caja, este valor sería el espacio entre la caja y lo que deseas guardar.

div {
    padding: 100px;
}

    Ejemplo de padding

Puedes establecer el padding en cada posición en una sola línea de las siguientes maneras:

    padding: [arriba] [derecha] [abajo] [izquierda], siguiendo el sentido horario.
    padding: [arriba] [abajo] [derecha e izquierda], siguiendo el eje principal.
    padding: [arriba y abajo] [derecha e izquierda], siguiendo los ejes del elemento.

También estableciendo de manera individual los valores de cada posición:

div {
    padding-top: 10px;
    padding-bottom: 15px;
    padding-left: 20px;
    padding-right: 10px;
}

Qué es el espaciado externo del elemento HTML o margin

El margin consiste en el espacio entre el borde y otro elemento HTML. Si imaginamos una caja, es el espacio entre tu caja y otra caja.

div {
    margin: 10px;
}

    Ejemplo de margin

Puedes establecer el margin en cada posición en una sola línea de las siguientes maneras:

    margin: [arriba] [derecha] [abajo] [izquierda], siguiendo el sentido horario.
    margin: [arriba] [abajo] [derecha e izquierda], siguiendo el eje principal.
    margin: [arriba y abajo] [derecha e izquierda], siguiendo los ejes del elemento.

También estableciendo de manera individual los valores de cada posición:

div {
    margin-top: 10px;
    margin-bottom: 15px;
    margin-left: 20px;
    margin-right: 10px;
}

Qué son los valores por defecto

Por defecto, el navegador establece valores iniciales a algunas propiedades CSS, este es el caso de margin y padding. Una buena práctica es utilizar el selector universal para restablecer estos valores a 0, para que no surjan errores inesperados.

* {
    margin: 0;
    padding: 0;
}

Qué es el tamaño total del elemento

El tamaño total del elemento está determinado por la suma de los valores de las propiedades border padding y widtho height, dependiendo del eje. La propiedad margin no está incluida en este cálculo.

Por ejemplo, definimos los siguientes estilos:

div{
  width: 150px;
  height: 150px;
  padding: 20px;
  border: 10px solid gray;
  margin: 30px;
}

    Ejemplo de medidas totales

El tamaño total del elemento será de 210px en ambos ejes, donde la suma fue: 150 (altura/anchura) + 20 x 2 (padding ambos lados) + 10 x 2 (borde ambos lados). Si evaluamos este elemento en las herramientas del desarrollador mostrará su tamaño como 210x210.

Aunque se conozca las medidas de los elementos de esta manera, no siempre existirá un control total. Por lo que podríamos establecer el tamaño total del elemento con width y height, y no solo del contenido, añadiendo la propiedad box-sizing.
Propiedad box-sizing

La propiedad box-sizing establece cómo se calculará el width y el height si incluyen bordes y espacios internos. Como buena práctica, se lo coloca en el selector universal, para que todos los elementos sigan esta tendencia.

* {
  box-sizing: border-box;
}

Con el valor border-box, el tamaño total del elemento será igual al especificado en el width y height, provocando que las medidas del contenido cambien con respecto a los bordes y espacios internos.

Por ejemplo, con los estilos que definimos anteriormente, establezcamos esta nueva propiedad.

    Ejemplo de box-sizing

El tamaño total del elemento será de 150px en ambos ejes, donde se calcularon las medidas del contenido para que la suma total sea lo especificado en el width y height. Si evaluamos este elemento en las herramientas del desarrollador mostrará su tamaño total como 150x150 y el contenido como 90x90.

Conclusión, establece las medidas totales del elemento con width y height, junto con box-sizing: border-box, para que el contenido se adecue a las necesidades del contenedor.
¿Cuál es el problema con el tamaño de los bordes?

Recapitulando, el tamaño total de un elemento es la suma de tres: el borde, el espacio interior y el contenido.

Entonces, en algunas ocasiones tendrás la intención de añadir un borde al realizar un hover. Esto provocará que el elemento necesite más espacio del inicial, en un contenedor con más elementos puede ocasionar un conflicto.

Mira el siguiente ejemplo, e intenta poner el cursor sobre un elemento ¿qué sucede?

    Ejemplo de problema con bordes

Observaste este comportamiento, debes tener cuidado con lo que agregas porque puedes provocar errores.

La solución a esto es colocar un borde de color transparent (transparente) y del mismo tamaño que el otro borde. Esto hará que el elemento se mantenga en su tamaño total, lo único que cambia es el color.

    Solución al problema

Evita agregar un tamaño diferente al inicial.

# LECTURA RECOMENDADA 

https://github.com/platzi/curso-frontend-developer/blob/5108689bdb6599cc92bd9595db28784f9be48704/curso-1/modelo-de-caja.html

https://www.joshwcomeau.com/css/rules-of-margin-collapse/

https://learn-the-web.algonquindesign.ca/topics/flexbox/