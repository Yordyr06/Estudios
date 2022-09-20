# -- TRABAJANDO CON TEXTO EN PYTHON: SLICES (REBANADAS) --

# En Python, los slices, traducidos al español como “rebanadas”,
# nos permiten dividir los caracteres de un string de múltiples formas.
# A continuación, realizaremos un ejemplo cómo utilizarlos:

# -- CÓMO USAR SLICES EN PYTHON --

nombre = "Francisco"
nombre
"Francisco"

nombre[0 : 3]
# Arranca desde el primer índice hasta llegar antes del 3° índice.
# El resultado sería: "Fra"

nombre[:3]
# Va desde el principio hasta antes de llegar del 3° índice. Como no
# hay ningún parámetro en el primer lugar, se interpreta que arranca
# desde el principio. Recordemos que empezamos a contar desde cero como
# primer dígito. El resultado sería: "Fra"

nombre[1:7]
# Arranca desde el índice 1 hasta llegar antes del 7.
# El resultado sería: "rancis"

nombre[1:7:2]
# Arranca desde el índice 1 hasta llegar antes del 7, pero pasos de 2 en 2,
# ya que eso es lo que nos indica el 3er parámetro, el cual es 2.
# El resultado sería: "rni"

nombre[1::3]
# Arranca desde el índice 1 hasta el final del string (al no haber ningún 2°
# parámetro, significa que va hasta el final), pero en pasos de 3 en 3.
# El resultado sería: "rcc"

nombre[::-1]
# Al no haber parámetro en las 2 primeras posiciones, se interpreta que se
# arranca desde el inicio hasta el final, pero en pasos de 1 en 1 con la
# palabra al revés, porque es -1.
# El resultado sería: "ocsicnarF"