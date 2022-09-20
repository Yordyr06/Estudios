# Responsive Design
El diseño responsivo (Responsive Design) consiste en un conjunto de herramientas para que tu sitio se vea bien en varias medidas de pantalla, esto incluye imágenes, tipografía, internacionalización de la página y entre otros.

En la actualidad, la mayoría de sitios web son visitados desde un celular, por lo que asegurarse que nuestro sitio sea responsivo para cualquier dispositivo es fundamental para optimizar las ganancias.

## Qué son las media queries
Las media queries son reglas CSS que establecen un comportamiento distinto o diferentes estilos en un cierto rango de la pantalla. Esto sirve para establecer el layout del sitio web para diferentes tipos de pantalla: escritorio, tablets y celulares.

Estos son dos tipos de media querie :

    max-width / max-height: establece un rango máximo para cierto comportamiento.
    min-width / min-height: establece un rango mínimo para cierto comportamiento.

Estos valores son parecidos a condicionales, mientras se cumpla la condición, aplica determinados estilos.
Estructura de la media querie

La estructura de una media querie consiste en empezar con @media, seguido del tipo de la media querie estableciendo un rango, envolviendo las reglas CSS dentro de ese rango.

[![](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer31.png)](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer31.png)

```css
@media (max-width:750px){
    div {
        color: red;
    }
    p {
        background-color: red;
    }
}
```

Herramientas del desarrollador para media queries

Para observar que los cambios se estén aplicando correctamente, las herramientas de desarrollador serán de gran ayuda.

Abre las herramientas del navegador y da clic en la opción “Toggle device tool”, aquí podrás manipular la pantalla y observar en cuántos píxeles está ocurriendo determinados estilos.

[![](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer32.png)](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer32.png)

[![](https://static.platzi.com/media/user_upload/3e9c6cff4c572339adf125abbb338c52-99fce187-34de-4445-9f35-17151a431374.jpg)](https://static.platzi.com/media/user_upload/3e9c6cff4c572339adf125abbb338c52-99fce187-34de-4445-9f35-17151a431374.jpg)

Utiliza el siguiente ejemplo para visualizar cómo cambian los estilos según la longitud de la pantalla. Puedes revisar la media querie que está en el código. Aunque solo cambien el color de dos elementos, puede estar cualquier propiedad que desees, prueba con todo.

    Ejemplo de media queries



# LECTURA RECOMENDADA:
https://github.com/platzi/curso-frontend-developer/blob/5108689bdb6599cc92bd9595db28784f9be48704/curso-1/diseno-responsivo.html

# REFERENCIA:
https://platzi.com/clases/2467-frontend-developer/40845-responsive-design/