# Tipos de selectores: básicos y combinadores

El selector define el elemento o conjunto de elementos HTML a los cuales se añadirán estilos. Existen [nombres de colores propios de CSS][colores] que puedes explorar. A continuación veamos más sobre selectores.
[colores]: https://htmlcolorcodes.com/es/nombres-de-los-colores/ "colore CSS"

## Cuáles son los selectores básicos
Un selector básico es la mínima expresión CSS para colocar estilos.

```css
selector {
    /* Estilos */
}
```

### 1. Selector de tipo
Selecciona todos los elementos que coincidan con el nombre de la etiqueta HTML.

```css
div {
    /* Todos los div en el documento */
}
```

#### Desafío de selector de tipo
Intenta dar un color de fondo a 10 etiquetas `<div>` con un solo selector, utiliza la propiedad background-color:

- [Desafío selector de tipo][desafioSelector]
[desafioSelector]: https://codi.link/PGRpdj5Tb3kgZWwgZGl2IDE8L2Rpdj4NCjxkaXY+U295IGVsIGRpdiAyPC9kaXY+DQo8ZGl2PlNveSBlbCBkaXYgMzwvZGl2Pg0KPGRpdj5Tb3kgZWwgZGl2IDQ8L2Rpdj4NCjxkaXY+U295IGVsIGRpdiA1PC9kaXY+DQo8ZGl2PlNveSBlbCBkaXYgNjwvZGl2Pg0KPGRpdj5Tb3kgZWwgZGl2IDc8L2Rpdj4NCjxkaXY+U295IGVsIGRpdiA4PC9kaXY+DQo8ZGl2PlNveSBlbCBkaXYgOTwvZGl2Pg0KPGRpdj5Tb3kgZWwgZGl2IDEwPC9kaXY+%7CLypBZ3JlZ2EgZWwgc2VsZWN0b3IgYXF1w60gKi8NCg0KLypBZ3JlZ2EgZWwgc2VsZWN0b3IgYXF1w60gKi8NCg0KDQovKiBJZ25vcmEgZXN0bywgcG9yIGFob3JhICovDQoqIHsNCiAgZm9udC1zaXplOiAxLjVyZW07DQogIG1hcmdpbi1ib3R0b206IDEwcHg7DQp9%7C "Desafío selector de tipo"
- [Solución al desafío][solucionSelector]
[solucionSelector]: https://codi.link/PGRpdj5Tb3kgZWwgZGl2IDE8L2Rpdj4NCjxkaXY+U295IGVsIGRpdiAyPC9kaXY+DQo8ZGl2PlNveSBlbCBkaXYgMzwvZGl2Pg0KPGRpdj5Tb3kgZWwgZGl2IDQ8L2Rpdj4NCjxkaXY+U295IGVsIGRpdiA1PC9kaXY+DQo8ZGl2PlNveSBlbCBkaXYgNjwvZGl2Pg0KPGRpdj5Tb3kgZWwgZGl2IDc8L2Rpdj4NCjxkaXY+U295IGVsIGRpdiA4PC9kaXY+DQo8ZGl2PlNveSBlbCBkaXYgOTwvZGl2Pg0KPGRpdj5Tb3kgZWwgZGl2IDEwPC9kaXY+%7CZGl2ew0KICBiYWNrZ3JvdW5kLWNvbG9yOiBhcXVhOw0KfQ0KDQovKiBJZ25vcmEgZXN0bywgcG9yIGFob3JhICovDQoqIHsNCiAgZm9udC1zaXplOiAxLjVyZW07DQogIG1hcmdpbi1ib3R0b206IDEwcHg7DQp9%7C "Solución al desafío"

### 2. Selector de clase
Selecciona todos los elementos que coincidan con las etiquetas HTML que contengan el atributo

```html
<!--archivo HTML-->
<div class="card"> Soy una carta </div>
```

Para seleccionar estos elementos, se empieza por un punto . y seguido el valor exacto del atributo class de la etiqueta. Puede ser cualquier valor que desees colocar.

```css
/* archivo CSS */
.card {
    /* Todas las etiquetas con la clase "card" */
}
```

Puede existir más de un valor dentro del atributo class separados por espacios.

```html
<!--archivo HTML-->
<div class="card card1"> Soy una carta </div>
<div class="card card2"> Soy una carta </div>
```

```css
.card {
    /* Todas las etiquetas con la clase "card" */
}

.card1 {
    /* Todas las etiquetas con la clase "card1" */
}

.card2 {
    /* Todas las etiquetas con la clase "card2" */
}
```

#### Desafío de selector de clase
De un conjunto de etiquetas `<div>` intenta dar un color de fondo a las etiquetas que contengan la clase `"card"` con un solo selector. Después, intenta dar un color de letra diferente para las etiquetas que contengan `"card1"` y `"card2"`

- [Desafío selector de clase][desafioSelector]
[desafioSelector]: https://codi.link/PGRpdj5Tb3kgZWwgZGl2IDE8L2Rpdj4NCjxkaXY+U295IGVsIGRpdiAyPC9kaXY+DQo8ZGl2IGNsYXNzPSJjYXJkIGNhcmQxIj5Tb3kgY2FyZC0xPC9kaXY+DQo8ZGl2PlNveSBlbCBkaXYgMzwvZGl2Pg0KPGRpdj5Tb3kgZWwgZGl2IDQ8L2Rpdj4NCjxkaXYgY2xhc3M9ImNhcmQiPlNveSBzb2xvIGNhcmQ8L2Rpdj4NCjxkaXY+U295IGVsIGRpdiA1PC9kaXY+DQo8ZGl2PlNveSBlbCBkaXYgNjwvZGl2Pg0KPGRpdj5Tb3kgZWwgZGl2IDc8L2Rpdj4NCjxkaXYgY2xhc3M9ImNhcmQgY2FyZDIiPlNveSBjYXJkLTI8L2Rpdj4NCjxkaXY+U295IGVsIGRpdiA4PC9kaXY+DQo8ZGl2PlNveSBlbCBkaXYgOTwvZGl2Pg0KPGRpdj5Tb3kgZWwgZGl2IDEwPC9kaXY+|LypBZ3JlZ2EgbG9zIHNlbGVjdG9yZXMgYXF1w60gKi8NCg0KLypBZ3JlZ2EgbG9zIHNlbGVjdG9yZXMgYXF1w60gKi8NCg0KDQovKiBJZ25vcmEgZXN0bywgcG9yIGFob3JhICovDQoqIHsNCiAgZm9udC1zaXplOiAxLjVyZW07DQogIG1hcmdpbi1ib3R0b206IDEwcHg7DQp9| "Desafío selector de clase"
- [Solución al desafío][solucionSelector]
[solucionSelector]: https://codi.link/PGRpdj5Tb3kgZWwgZGl2IDE8L2Rpdj4NCjxkaXY+U295IGVsIGRpdiAyPC9kaXY+DQo8ZGl2IGNsYXNzPSJjYXJkIGNhcmQxIj5Tb3kgY2FyZC0xPC9kaXY+DQo8ZGl2PlNveSBlbCBkaXYgMzwvZGl2Pg0KPGRpdj5Tb3kgZWwgZGl2IDQ8L2Rpdj4NCjxkaXYgY2xhc3M9ImNhcmQiPlNveSBzb2xvIGNhcmQ8L2Rpdj4NCjxkaXY+U295IGVsIGRpdiA1PC9kaXY+DQo8ZGl2PlNveSBlbCBkaXYgNjwvZGl2Pg0KPGRpdj5Tb3kgZWwgZGl2IDc8L2Rpdj4NCjxkaXYgY2xhc3M9ImNhcmQgY2FyZDIiPlNveSBjYXJkLTI8L2Rpdj4NCjxkaXY+U295IGVsIGRpdiA4PC9kaXY+DQo8ZGl2PlNveSBlbCBkaXYgOTwvZGl2Pg0KPGRpdj5Tb3kgZWwgZGl2IDEwPC9kaXY+%7CLypBZ3JlZ2EgbG9zIHNlbGVjdG9yZXMgYXF1w60gKi8NCi5jYXJkIHsNCiAgYmFja2dyb3VuZC1jb2xvcjogYXF1YTsNCn0NCg0KLmNhcmQxew0KICBjb2xvcjogcmVkOw0KfQ0KDQouY2FyZDJ7DQogIGNvbG9yOiBibHVlOw0KfQ0KLypBZ3JlZ2EgbG9zIHNlbGVjdG9yZXMgYXF1w60gKi8NCg0KDQovKiBJZ25vcmEgZXN0bywgcG9yIGFob3JhICovDQoqIHsNCiAgZm9udC1zaXplOiAxLjVyZW07DQogIG1hcmdpbi1ib3R0b206IDEwcHg7DQp9%7C "Solución al desafío"

### 3. Selector de identificador único (id)
Selecciona el único elemento que coincida con la etiqueta HTML que contenga el atributo `id`. Solo puede existir un valor `id` para todo el documento.

```html
<!--archivo HTML-->
<button id="eliminar"> Eliminar  </button>
```

Para seleccionar el elemento, se empieza por el símbolo de hashtag `#` y seguido el valor exacto del atributo `id` de la etiqueta. Puede ser cualquier valor que desees colocar.

```css
/* archivo CSS */
#eliminar {
    /* La única etiqueta con el id "eliminar" */
}
```

#### Desafío de selector de ID
De un conjunto de etiquetas `<button>`, existe un único botón para eliminar. Intenta colocar un color de fondo rojo a este elemento.

- [Desafío selector de ID][desafioID]
[desafioID]: https://codi.link/PGJ1dHRvbj5Tb3kgZWwgYnV0dG9uIDE8L2J1dHRvbj4NCjxidXR0b24+U295IGVsIGJ1dHRvbiAyPC9idXR0b24+DQo8YnV0dG9uPlNveSBlbCBidXR0b24gMzwvYnV0dG9uPg0KPGJ1dHRvbj5Tb3kgZWwgYnV0dG9uIDQ8L2J1dHRvbj4NCjxidXR0b24+U295IGVsIGJ1dHRvbiA1PC9idXR0b24+DQo8YnV0dG9uPlNveSBlbCBidXR0b24gNjwvYnV0dG9uPg0KPGJ1dHRvbj5Tb3kgZWwgYnV0dG9uIDc8L2J1dHRvbj4NCjxidXR0b24+U295IGVsIGJ1dHRvbiA4PC9idXR0b24+DQo8YnV0dG9uPlNveSBlbCBidXR0b24gOTwvYnV0dG9uPg0KPGJ1dHRvbiBpZD0iZWxpbWluYXIiPsKhRWxpbcOtbmFsbyEhISEhISEhPC9idXR0b24+%7CLypBZ3JlZ2EgbG9zIHNlbGVjdG9yZXMgYXF1w60gKi8NCg0KLypBZ3JlZ2EgbG9zIHNlbGVjdG9yZXMgYXF1w60gKi8NCg0KDQovKiBJZ25vcmEgZXN0bywgcG9yIGFob3JhICovDQoqIHsNCiAgZm9udC1zaXplOiAxLjJyZW07DQogIHBhZGRpbmc6IDVweDsNCiAgbWFyZ2luLWJvdHRvbTogMTBweDsNCn0=%7C "Desafío selector de ID"
- [Solución al desafío][solucionID]
[solucionID]: https://codi.link/PGJ1dHRvbj5Tb3kgZWwgYnV0dG9uIDE8L2J1dHRvbj4NCjxidXR0b24+U295IGVsIGJ1dHRvbiAyPC9idXR0b24+DQo8YnV0dG9uPlNveSBlbCBidXR0b24gMzwvYnV0dG9uPg0KPGJ1dHRvbj5Tb3kgZWwgYnV0dG9uIDQ8L2J1dHRvbj4NCjxidXR0b24+U295IGVsIGJ1dHRvbiA1PC9idXR0b24+DQo8YnV0dG9uPlNveSBlbCBidXR0b24gNjwvYnV0dG9uPg0KPGJ1dHRvbj5Tb3kgZWwgYnV0dG9uIDc8L2J1dHRvbj4NCjxidXR0b24+U295IGVsIGJ1dHRvbiA4PC9idXR0b24+DQo8YnV0dG9uPlNveSBlbCBidXR0b24gOTwvYnV0dG9uPg0KPGJ1dHRvbiBpZD0iZWxpbWluYXIiPsKhRWxpbcOtbmFsbyEhISEhISEhPC9idXR0b24+|LypBZ3JlZ2EgbG9zIHNlbGVjdG9yZXMgYXF1w60gKi8NCiNlbGltaW5hcnsNCiAgYmFja2dyb3VuZC1jb2xvcjogcmVkOw0KfQ0KLypBZ3JlZ2EgbG9zIHNlbGVjdG9yZXMgYXF1w60gKi8NCg0KDQovKiBJZ25vcmEgZXN0bywgcG9yIGFob3JhICovDQoqIHsNCiAgZm9udC1zaXplOiAxLjJyZW07DQogIHBhZGRpbmc6IDVweDsNCiAgbWFyZ2luLWJvdHRvbTogMTBweDsNCn0=| "Solución al desafío"

4. Selector de atributo

Selecciona los elementos que coincidan con la etiqueta HTML que contenga el atributo y valor especificado.

<!--archivo HTML-->
<a href="https://platzi.com"> Ir a Platzi </a>

Para seleccionar los elementos, se empieza por el nombre de la etiqueta, seguido de corchetes [] que contiene el atributo y valor especificado.

/* archivo CSS */
a[href=""https://platzi.com"] {
    /* Todas las etiquetas <a> con una propiedad href con valor "https://platzi.com" */
}

Desafío de selector de atributo

Intenta colocar un color de fondo a las etiquetas <a> que contengan el atributo href con el valor de "https://platzi.com".

    Desafío selector de atributo

    Solución al desafío

5. Selector universal

Selecciona todos los elementos del documento mediante un asterisco *.

* {
    /* Todos los elementos */
}

Desafío de selector universal

Intenta colocar un color de fondo a todos los elementos del documento.

    Desafío selector universal

    Solución al desafío

## Cuáles son los selectores combinadores

Un selector combinador es la unión de dos o más selectores básicos.

selector1 selector2 selector3 {
    /* Estilos */
}

1. Combinador de descendientes

Selecciona todos los elementos del selector de la derecha que son hijos del selector de la izquierda, independientemente de la profundidad. Estos selectores están separados por un espacio.

padre hijos {
    /* Todos los hijos del padre */
}

div p{
    /* Todos los hijos <p> de <div>*/
}

.container img{
    /* Todos los hijos <img> de la clase "container"*/
}

Desafío del combinador de descendientes

Intenta colocar un color de letra a todas las etiquetas <li> que son hijos de la clase "container".

    Desafío combinador de descendientes

    Solución al desafío

2. Combinador de hijo directo

Selecciona todos los elementos del selector de la derecha que son hijos directos del selector de la izquierda. Estos selectores están separados por >.

padre > hijos_directos {
    /* Todos los hijos directos del padre */
}

div > p{
    /* Todos los hijos directos <p> de <div>*/
}

.container > img{
    /* Todos los hijos directos <img> de la clase "container"*/
}

Desafío de combinador de hijo directo

Intenta colocar un color de letra a todos las etiquetas <p> que son hijos directos de la clase "container".

    Desafío combinador de hijo directo

    Solución al desafío

3. Combinador de elemento adyacente

Selecciona todos los elementos del selector de la derecha que están adyacente al selector de la izquierda. Estos selectores están separados por +.

elemento + adyacente {
    /* Elementos adyacentes */
}

div + p{
    /* Todos los <p> adyacentes a <div>*/
}

.container + img{
    /* Todos los <img> adyacentes a la clase "container"*/
}

Adyacente significa que comparten el mismo padre y está situado inmediatamente hacia abajo de otro elemento. Por ejemplo, en el siguiente código, <div> está adyacente a <h1> y <p> está adyacente a <div>. Sin embargo, <h1> no está adyacente a <div> y <div> no está adyacente a <p>.

<!--archivo HTML -->
<h1>Soy un título </h1>
<div>Soy un div</div>
<p>Soy un párrafo</p>

Desafío de combinador de elemento adyacente

Intenta colocar un color de letra a todos las etiquetas <p> que están adyacente a las etiquetas <div>.

    Desafío combinador de elemento adyacente

    Solución al desafío

4. Combinador general de hermanos

Selecciona todos los elementos del selector de la derecha que son hermanos del selector de la izquierda. Estos selectores están separados por ~.

elemento + adyacente {
    /* Elementos adyacentes */
}

div + p{
    /* Todos los <p> adyacentes a <div>*/
}

.container + img{
    /* Todos los <img> adyacentes a la clase "container"*/
}

Hermanos significa que comparten el mismo padre y están situados hacia abajo de otro elemento. Por ejemplo, en el siguiente código, <div> y <p> son hermanos de <h1>, pero <h1> no es hermano de <div> y <p>.

<!--archivo HTML -->
<h1>Soy un título </h1>
<div>Soy un div</div>
<p>Soy un párrafo</p>

Desafío de combinador general de hermanos

Intenta colocar un color de letra a todos las etiquetas <p> que son hermanos de <div>.

    Desafío combinador general de hermanos

    Solución al desafío


# Lecturas recomendadas

    https://htmlcolorcodes.com/es/
    https://github.com/platzi/curso-frontend-developer/blob/5108689bdb6599cc92bd9595db28784f9be48704/curso-1/selectores-2.html