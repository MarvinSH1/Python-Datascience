# #Entrenando la programación
# 1 - Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el número más grande.
""" numero1=int(input("Ingresa el primer numero: "))
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
    print("El numero es decimal") """

#10 - Un programa debe ser escrito para leer dos números y luego preguntar a la persona usuaria qué operación desea realizar. El resultado de la operación debe incluir información sobre el número, si es par o impar, positivo o negativo, e entero o decimal.
""" numero1=float(input("Ingresa el primer numero: "))
numero2=float(input("Ingresa el segundo numero: "))

operacion=input("¿Qué operación deseas realizar? (suma, resta, multiplicación, división): ").lower()

if(operacion == "suma"):
    resultado=numero1+numero2
    print(f"El resultado de la suma es {resultado} y es un número {"par,\n" if resultado%2==0 else "impar,\n"} es {"positivo," if resultado>0 else "negativo" if resultado<0 else "cero"} y  es {"entero." if resultado.is_integer() else "decimal."}") 
    print(resultado.is_integer())
elif(operacion == "resta"):
    resultado=numero1-numero2
    print(f"El resultado de la resta es {resultado} y es un número {"par,\n" if resultado%2==0 else "impar,\n"} es {"positivo," if resultado>0 else "negativo" if resultado<0 else "cero"} y  es {"entero." if resultado.is_integer() else "decimal."}") 
elif(operacion == "multiplicación"):
    resultado=numero1*numero2
    print(f"El resultado de la multiplicación es {resultado} y es un número {"par,\n" if resultado%2==0 else "impar,\n"} es {"positivo," if resultado>0 else "negativo" if resultado<0 else "cero"} y  es {"entero." if resultado.is_integer() else "decimal."}") 
elif(operacion == "división"):
    if numero2!=0:
        resultado=numero1/numero2
        print(f"El resultado de la división es {resultado} y es un número {"par,\n" if resultado%2==0 else "impar,\n"} es {"positivo," if resultado>0 else "negativo" if resultado<0 else "cero"} y  es {"entero." if resultado.is_integer() else "decimal."}") 
    else:
        print("No se puede dividir entre cero")
else:
    print("Operación no válida")
 """
"""11 - Escribe un programa que pida a la persona usuaria tres números que representan los lados de un triángulo. El programa debe informar si los valores pueden utilizarse para formar un triángulo y, en caso afirmativo, si es equilátero, isósceles o escaleno. Ten en cuenta algunas sugerencias:
Tres lados forman un triángulo cuando la suma de cualesquiera dos lados es mayor que el tercero;
Triángulo Equilátero: tres lados iguales;
Triángulo Isósceles: dos lados iguales;
Triángulo Escaleno: tres lados diferentes.
"""
""" print("Ingresa los lados de un triángulo")
lado1=float(input("Ingresa el primer lado: "))
lado2=float(input("Ingresa el segundo lado: "))
lado3=float(input("Ingresa el tercer lado: "))

if (lado1+lado2>lado3) and (lado1+lado3>lado2) and (lado2+lado3>lado1):
    if lado1==lado2==lado3:
        print("El triángulo es equilátero")
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")
 """

"""
12 - Un establecimiento está vendiendo combustibles con descuentos variables. Para el etanol, si la cantidad comprada es de hasta 15 litros, el descuento será del 2% por litro. En caso contrario, será del 4% por litro. Para el diésel, si la cantidad comprada es de hasta 15 litros, el descuento será del 3% por litro. En caso contrario, será del 5% por litro. El precio por litro de diésel es de R$ 2,00 y el precio por litro de etanol es de R$ 1,70. Escribe un programa que lea la cantidad de litros vendidos y el tipo de combustible (E para etanol y D para diésel) y calcule el valor a pagar por el cliente. Ten en cuenta algunas sugerencias:
El valor del descuento será el producto del precio por litro, la cantidad de litros y el valor del descuento.
El valor a pagar por un cliente será el resultado de la multiplicación del precio por litro por la cantidad de litros menos el valor del descuento resultante del cálculo.
"""
""" precioLitroDiesel=2.00
precioLitroEtanol=1.70

print("Bienvenido a la estación de servicio")
combustible=input("¿Qué tipo de combustible desea? (E para etanol, D para diésel): ").upper()

if(combustible=="E" or combustible=="D"):
    try:
        litrosComprar=float(input(f"Cuántos litros desea comprar? (costo: ${precioLitroEtanol if combustible=="E" else precioLitroDiesel} por litro): "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        litrosComprar=0

    if(litrosComprar>0 and litrosComprar<=15):
        totalSinDescuento=(precioLitroEtanol if combustible=="E" else precioLitroDiesel) *litrosComprar
        descuento=(totalSinDescuento*0.02) if combustible=="E" else (totalSinDescuento*0.03)
        totalConDescuento=totalSinDescuento-descuento
        print(f"Genial! usted tiene un descuento del {"2%" if combustible=="E" else "3%"} y paga ${totalConDescuento}, antes ${totalSinDescuento}")
    elif(litrosComprar>15):
        totalSinDescuento=(precioLitroEtanol if combustible=="E" else precioLitroDiesel) *litrosComprar
        descuento=(totalSinDescuento*0.04) if combustible=="E" else (totalSinDescuento*0.05)
        totalConDescuento=totalSinDescuento-descuento
        print(f"Genial! usted tiene un descuento del {"4%" if combustible=="E" else "5%"} y paga ${totalConDescuento}, antes ${totalSinDescuento}")
    else:
        print("La cantidad de litros debe ser un número válido")
    
else:
     print("Tipo de combustible no válido")

    
 """
"""
13 - En una empresa de venta de bienes raíces, debes crear un código que analice los datos de ventas anuales para ayudar a la dirección en la toma de decisiones. El código debe recopilar los datos de cantidad de ventas durante los años 2022 y 2023 y calcular la variación porcentual. A partir del valor de la variación, se deben proporcionar las siguientes sugerencias:
Para una variación superior al 20%: bonificación para el equipo de ventas.
Para una variación entre el 2% y el 20%: pequeña bonificación para el equipo de ventas.
Para una variación entre el 2% y el -10%: planificación de políticas de incentivo a las ventas.
Para bonificaciones inferiores al -10%: recorte de gastos.
"""
print("Bienvenido a la empresa de bienes raíces")
ventas2022=float(input("Ingrese la cantidad de ventas del año 2022: "))
ventas2023=float(input("Ingrese la cantidad de ventas del año 2023: "))

# Calcular la variación porcentual
variacion=((ventas2023-ventas2022)/ventas2022)*100
print(f"La variación porcentual es del {variacion:.2f}%")

if variacion>20:
    print("Bonificación para el equipo de ventas")
elif variacion>=2 and variacion<=20:
    print("Pequeña bonificación para el equipo de ventas")
elif variacion>=-10 and variacion<2:    
    print("Planificación de políticas de incentivo a las ventas")
elif variacion<-10:
    print("Recorte de gastos")