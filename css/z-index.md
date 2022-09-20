# Z-index y el contexto de apilamiento

El contexto de apilamiento consiste en la superposición de capas o elementos a lo largo del eje Z del navegador. Esto es importante para evitar que un elemento esté ocultando a otro.

[![](https://media1.giphy.com/media/1IvbqeWg7gLlRi2TAC/giphy.gif?cid=790b7611ba7156183cec0ef1ba9e76527d6adfbc2610e94c&rid=giphy.gif&ct=g)](https://media1.giphy.com/media/1IvbqeWg7gLlRi2TAC/giphy.gif?cid=790b7611ba7156183cec0ef1ba9e76527d6adfbc2610e94c&rid=giphy.gif&ct=g)

Qué son los planos y ejes
El navegador está constituido de tres planos y ejes: el ancho o X; el alto o Y; y el de profundidad o Z.

El eje X positivo está hacia la derecha; el eje Y positivo está hacia abajo; y el eje Z positivo está hacia el usuario.

[![](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/animationland03.PNG)](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/animationland03.PNG)

Estos son muy importantes para mover los elementos del HTML desde un punto inicial hacia un punto final.

## Qué es la propiedad z-index
El contexto de apilamiento se configura con la propiedad z-index.

Por defecto, todos los elementos tienen un valor auto, es decir, el orden está definido por la estructura del HTML. Los primeros elementos estarán detrás y los últimos estarán de frente.

Si se establece un valor positivo, este elemento se sitúa por delante de los demás. Si se establece un valor negativo, se sitúa por detrás.

Si un elemento tiene un z-index mayor a otro, estará por delante. Sin embargo, si un elemento que tiene un z-index menor a otros, sus hijos nunca estarán por encima, aunque su z-index sea mayor.

[![](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer27.png)](https://cdn.document360.io/da52b302-22aa-4a71-9908-ba18e68ffee7/Images/Documentation/frontend_developer27.png)


    Ejemplo de contexto de apilamientos

Como puedes observar en la imagen, el elemento con la clase yellow tiene un z-index mayor a red, pero no está por encima, porque su contexto de apilamiento está dentro del contexto de apilamiento del elemento blue, así mismo, nunca estará por detrás de su elemento padre.


# LECTURAS RECOMENDADAS

https://github.com/platzi/curso-frontend-developer/blob/5108689bdb6599cc92bd9595db28784f9be48704/curso-1/z-index.html

https://gist.github.com/teffcode/e0b3e89df22ecf5374527deaf31b11ca