# Unidades de medida

Las unidades de medida establecen una longitud para un determinado elemento o tipografía. Existen dos tipos de medidas: absolutas y relativas.

[![](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer29.png)](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer29.png)

## Qué son las medidas absolutas
Las medidas absolutas son valores fijos, por lo que la medida no cambiará. La unidad absoluta más utilizada son los píxeles px, las demás son muy poco utilizadas, pero es bueno que las conozcas.

## Qué son las medidas relativas
Las medidas relativas son valores variables, por lo que la medida depende de un valor externo. Se debe tener en cuidado con estas porque un pequeño cambio puede desencadenar tamaños muy elevados.

## Diferencia entre rem y em
La medida em depende del elemento que lo contiene, es decir, si un elemento tiene font-size de 20px, el valor de em es igual a 20px, el valor de 2em será de 40px y así sucesivamente.

La medida rem depende del elemento raíz, el valor del font-size del elemento raíz es de 16px, por lo tanto, el valor de 2rem es igual a 32px, y así sucesivamente.
    Ejemplo de medida em

En las herramientas del desarrollador, te muestra el tamaño de la fuente (font) en píxeles.
	Ejemplo de medida rem


## Diferencia entre porcentajes y la anchura y altura de la pantalla
Los porcentajes representan el tamaño con respecto al total del elemento padre. Si el elemento padre tiene 20px, entonces el 100% será de 20px.

Por otra parte, las medidas de anchura vw y altura vh representan el tamaño con respecto al total de la pantalla. Si el elemento tiene un tamaño de 100vw será el 100 por ciento de la pantalla.

Si un elemento tiene todo el tamaño de la pantalla, entonces solamente en ese punto la medida 100% será igual a 100vw o 100vh.

## Problema con las medidas de texto
Los navegadores tienen una opción para cambiar el tamaño del texto. Con medidas absolutas, el tamaño de la letra no cambiará, por lo que será un problema para el usuario.

Con medidas relativas, el tamaño cambiará con respecto a la fuente del elemento raíz. Por lo que estas son una buena opción para solucionar este problema de accesibilidad, en específico la medida rem.

Sin embargo, la medida rem equivale a 16px y puede ser confuso mientras utilices valores altos. Por lo que vamos a cambiar el valor del elemento de la raíz para que la medida rem sea igual a 10px.

En la etiqueta <html> cambia el valor de la propiedad font-size a 62.5%, resultado de una regla de tres: si 16px es igual al 100% entonces cuál será el porcentaje para 10px.

html {
    font-size: 62.5%;
}

Con este cambio, la medida rem será igual a 10px, ahora los puedes utilizar sin problema y tus textos cambiarán según las preferencias de usuario.


# LECTURA RECOMENDADA:
https://github.com/platzi/curso-frontend-developer/blob/5108689bdb6599cc92bd9595db28784f9be48704/curso-1/unidades-de-medida.html

# REFERENCIA:
https://platzi.com/clases/2467-frontend-developer/40844-unidades-de-medida/