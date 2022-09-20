# Anatomía de un documento HTML y sus elementos
Antes de empezar a escribir código HTML, debemos conocer la anatomía de un documento y sus elementos.

------------

## ¿Cuáles son los elementos HTML?¿Cuáles son los elementos HTML?

Los elementos son cada una de las partes que conforman un archivo HTML. Su estructura contiene:

    Etiquetas: es la representación de un elemento HTML. Se dividen en etiquetas de apertura, representadas por <etiqueta> y etiquetas de cierre, representadas por </etiqueta>.
    Contenido: es el texto o elementos encerrados por la etiqueta, este valor es opcional en algunas de ellas.


### Qué son atributos HTML

Los atributos HTML son propiedades en la etiqueta de apertura que manejan el comportamiento del elemento. Su valor está envuelto en comillas.

### Qué son los elementos vacíos

Los elementos vacíos son aquellos que únicamente se representan en una etiqueta de apertura. Por ejemplo, la etiqueta de imagen: <img...>.
Estas etiquetas pueden cerrarse en la misma etiqueta de apertura, utilizando la barra inclinada “/” al final: <img.../>,

### Qué es el anidamiento de elementos

El anidamiento de elementos HTML consiste en envolver varias etiquetas en otras etiquetas.

Interpreta a cada elemento HTML como una caja donde puedes guardar diferentes elementos u otras cajas. Estas cajas tendrán diferentes tamaños y estarán colocadas junto a otras.

	Aquellas etiquetas que envuelven a otras se las denomina "padres". Es decir, <section> es padre de <h1> </h1> <p>, <ul>, y a su vez <ul> es padre de 3 etiquetas <li>.
	Las etiquetas que son el contenido de otras, se las denomina “hijos”. Es decir, las etiquetas <h1>, <p>, <ul> son hijos de <section>, y a su vez las etiquetas <li> son hijos de <ul>.

## Estructura básica de un documento HTML

La estructura básica de un documento HTML está configurado por las siguientes etiquetas principales:

Etiqueta Doctype
La etiqueta <!DOCTYPE html> especifica que el archivo se maneje con la versión 5 de HTML.

Etiqueta html
La etiqueta <html> define el elemento raíz de un documento HTML. Todos los demás elementos deben estar contenidos dentro de este elemento raíz. En esta etiqueta se especifica el lenguaje de la página web mediante la propiedad lang.

Etiqueta head
La etiqueta <head> define la metainformación, es decir, toda información que no es contenido como tal de la página web. Por ejemplo, los enlaces a archivos CSS y JavaScript, el título y la imagen que aparecen en la pestaña del navegador. Esto es importante para motores de búsqueda como Google.

Etiqueta body
La etiqueta <body> define el contenido de la página web. Debe ser hijo cercano de <html> y padre de todas las etiquetas HTML, excepto por aquellas que definan metainformación.

Comentarios de HTML

Los comentarios de HTML consiste en señalar algo que se ignorará. Para establecer un comentario HTML se lo envuelve entre <!-- y -->, independiente de la cantidad de líneas.

<!-- Este es un comentario de una línea -->
<!--
Este es un comentario de varias líneas
-->

Desafío: construye la estructura de un documento HTML

Utiliza tu editor Visual Studio Code o la herramienta codi.link. Si utilizas codi.link puedes visualizar toda la página web en la opción “Preview”.
