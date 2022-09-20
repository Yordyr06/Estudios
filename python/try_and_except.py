# # -- INTRUCCIONES TRY Y EXCEPT --

# Aveces requerimos que sean validados cierto o ciertos bloques de código y así
# evitar errores de sintaxis, para eso ulizamos la instruccion de try y except
# que nos permitiran validar bloques de código para evitar errores futuros a la 
# hora de correr la aplicación. Veamos el siguiente ejemplo:

import string
no = input("Ingrese un número: ")
try: 
    no = int(no)
except:
    no = string
if no == string:
    print("Error, por favor ingrese un dato correcto")
else:
    print("El número ingresado fue: " + no)