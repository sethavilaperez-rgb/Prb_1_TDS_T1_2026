# 1. Número par o impar
print("1. Número par o impar")
numero = int(input("Ingresa un número entero: "))

"""
Si el residuo del número es 0 al dividirse entre 2 entonces el
operador ternario dara "Par", si no sera "Impar" ya que tiene residuo.
"""
resultado = "Par" if numero % 2 == 0 else "Impar"
print("El número es:", resultado)

# 2. Calificación
print("2. Calificación")
calificacion = int(input("Ingresa la calificación (0-100): "))

while calificacion < 0 or calificacion > 100:
    print("Calificación invalida")
    calificacion = int(input("Ingresa la calificación (0-100): "))
"""
Simplemente se utiliza un if principal para iniciar la condición de manera 
ordenada de mayor a menor para que cada 10 puntos sea una calificación  diferente,
con elif para las opciones posteriores y finalmente un else para todo lo demás abajo de 59.
"""

if calificacion >= 90:
    letra = "A"
elif calificacion >= 80:
    letra = "B"
elif calificacion >= 70:
    letra = "C"
elif calificacion >= 60:
    letra = "D"
else:
    letra = "F"

print("La calificación es:", letra)

# 3. Mayor de tres números
print("3. Mayor de tres números")
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

"""
Si a es mayor que b ahora solo queda verificar que a sea mayor que c para
saber quien es el mayor, en dado caso de que sea menor, c seria mayor y ese seria el 
resultado, ahora si a desde un principio es menor que b, solo quedaria verificar que b
sea mayor que c para poder dar un resultado.
"""
if a > b:
    if a > c:
        mayor = a
    else:
        mayor = c
else:
    if b > c:
        mayor = b
    else:
        mayor = c

print("El número mayor es:", mayor)


# 4. Verificación de edad
print("4. Verificación de edad")
edad = int(input("Ingresa tu edad: "))

"""
Un programa muy sencillo, simplemente con una condición if y una variable se pregunta si la edad
es mayor o igual a 18, si es mayor es mayor de edad y si no es menor de edad
"""
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# 5. Descuento por compra
print("5. Descuento por compra")
monto = float(input("Ingresa el monto total de la compra: "))

"""
Si el monto es mayor de 1000 se le resta el 10% del monto al mismo
monto
"""
if monto > 1000:
    monto -= monto * 0.10

print("Monto a pagar:", monto)


# 6. Número positivo, negativo o cero
print("6. Número positivo, negativo o cero")
numero = float(input("Ingresa un número: "))

"""
Con una variable recogemos un numero flotante, si este es mayor a 0
será positivo, si es menor a 0 sera negativo, los condicionales mayor y menor
que son importantes que no sean mayor igual o menor igual, ya que
todo lo que no sea 0 tendra la condición.
"""
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")


# 7. Día de la semana
print("7. Día de la semana")
dia = int(input("Ingresa un número del 1 al 7: "))

"""
Esta contruido de la misma manera que el segundo ejercicio,
utilizando if, elif y else para controlar el resultado de la variable y 
poder imprimir el dia de la semana, adicional si se coloca un numeo que no sea del 1
al 7 sera invalido
"""
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("Número inválido")
