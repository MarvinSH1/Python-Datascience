# #Entrenando la programación
# 1 - Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el número más grande.
numero1=int(input("Ingresa el primer numero: "))
numero2=int(input("Ingresa el segundo numero: "))
if numero1>numero2:
    print("El numero mayor esx:",numero1)
elif numero1<numero2:
    print("El numero mayor esz:",numero2)
else:
    print("Ambos numeros son iguales")

# 2 - Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa e informe si hubo un crecimiento (porcentaje positivo) o una disminución (porcentaje negativo).
porcentajeAnterior=float(input("Ingresa el porcentaje de crecimiento de produccion del año pasado: "))
porcentajeActual=float(input("Ingresa el porcentaje de crecimiento de produccion actual: "))

if(porcentajeActual>porcentajeAnterior):
    crecimiento=porcentajeActual-porcentajeAnterior
    print("Hubo un crecimiento de produccion de ", crecimiento, "%")
elif(porcentajeActual<porcentajeAnterior):
    disminucion=porcentajeAnterior-porcentajeActual
    print("Hubo una disminucion de produccion de ", disminucion, "%")
else:
    print("No hubo cambios en la produccion de la empresa.", porcentajeActual, "%")

# 3 - Escribe un programa que determine si una letra proporcionada por la persona usuaria es una vocal o una consonante.
letra=input("Ingresa una letra: ").upper()
if letra in "AEIOU":
    print("Es una vocal")
else:
    print("Es una consonante")

# 4 - Escribe un programa que lea valores promedio de precios de un modelo de automóvil durante 3 años consecutivos y muestre el valor más alto y más bajo entre esos tres años.
primerAnio=float(input("Precio del auto en el primer año: "))
segundoAnio=float(input("Precio del auto en el segundo año: "))
tercerAnio=float(input("Precio del auto en el tercer año: "))

valorAlto=max(primerAnio, segundoAnio, tercerAnio)
valorBajo=min(primerAnio, segundoAnio, tercerAnio)
print("El valor más alto es:", valorAlto)
print("El valor más bajo es:", valorBajo)

promedio=(primerAnio+segundoAnio+tercerAnio)/3
print("El promedio de los precios es:", promedio)
# 5 - Escribe un programa que pregunte sobre el precio de tres productos e indique cuál es el producto más barato para comprar.
precioUno=float(input("Ingresa el precio del primer producto: "))
precioDos=float(input("Ingresa el precio del segundo producto: ")) 
precioTres=float(input("Ingresa el precio del tercer producto: "))

print("precio minimo", min(precioUno, precioDos, precioTres))    

# 6 - Escribe un programa que lea tres números y los muestre en orden descendente.
numero1=int(input("Ingresa el primer numero: "))
numero2=int(input("Ingresa el segundo numero: "))
numero3=int(input("Ingresa el tercer numero: "))

ordenados=[numero1, numero2, numero3]
ordenados.sort(reverse=True)   
print("Los numeros en orden descendente son:",ordenados)

# 7 -Escribe un programa que pregunte en qué turno estudia la persona usuaria ("mañana", "tarde" o "noche") y muestre el mensaje "¡Buenos Días!", "¡Buenas Tardes!", "¡Buenas Noches!" o "Valor Inválido!", según el caso.
nombre=input("Ingresa tu nombre por favor: ")
turno=input("¿En qué turno estudias? (mañana, tarde o noche): ").lower()

if turno == "mañana":
    print("¡Buenos Días, " + nombre)
elif turno == "tarde":
    print("¡Buenas Tardes, " + nombre)    
elif turno == "noche":
    print("¡Buenas Noches, " + nombre)
else:
    print("Valor Inválido, " + nombre)

# 8 - Escribe un programa que solicite un número entero a la persona usuaria y determine si es par o impar. Pista: Puedes usar el operador módulo (%).
numero=int(input("Ingresa un numero entero: "))

if(numero%2==0):
    print("El numero es par")
else:
    print("El numero es impar")

# 9 - Escribe un programa que pida un número a la persona usuaria y le informe si es entero o decimal.
numero=float(input("Ingresa un numero: "))

if numero.is_integer():
    print("El numero es entero")
else:
    print("El numero es decimal")