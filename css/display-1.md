# Tipos de display más usados: block, inline e inline-block

La propiedad display establece el tipo de visualización de los elementos HTML sin afectar el flujo normal de los elementos.

Existen etiquetas que por defecto su display ya está determinado, como la etiqueta <div> que tiene display block, <span> tiene display inline y <button> tiene display inline-block.

Abordaremos los tipos de display block, inline e inline-block a continuación.
Visualización en bloque (block)

El display block **establece que un elemento ocupará todo el espacio disponible por defecto y el siguiente elemento a este se situará por debajo.

Es posible añadir medidas de anchura width y altura height a estos a elementos.

También es posible agregar todas las propiedades del modelo de caja (no te preocupes de este concepto, ya lo abordaremos).

    Ejemplo de display block

Visualización en línea (inline)

El display inline establece que un elemento ocupará el espacio del contenido del mismo y el siguiente elemento se situará a la derecha.

No es posible añadir medidas de anchura width y altura height a estos a elementos.

También, no es posible agregar todas las propiedades del modelo de caja, únicamente funcionará la propiedad margin en el eje horizontal (no te preocupes de este concepto, ya lo abordaremos).

    Ejemplo de display inline

Visualización de bloque y línea (inline-block)

El display inline-block combina las ventajas de bloque de colocar medidas al elemento y propiedades del modelo de caja correctamente; con las ventajas de inline de color un elemento seguido de otro en el mismo espacio.

Si elemento excede el contenido total, se coloca en la siguiente línea por debajo.

    Ejemplo de display inline-block

Visualización nula (none)

El display none desactiva la visualización de un elemento, como si el elemento no existiera.

    Ejemplo de display none
