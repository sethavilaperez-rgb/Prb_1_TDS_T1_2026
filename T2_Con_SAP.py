# 1. Número par o impar
print("1. Número par o impar")
numero = int(input("Ingresa un número entero: "))

resultado = "Par" if numero % 2 == 0 else "Impar"
print("El número es:", resultado)

# 2. Calificación
print("2. Calificación")
calificacion = int(input("Ingresa la calificación (0-100): "))

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

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# 5. Descuento por compra
print("5. Descuento por compra")
monto = float(input("Ingresa el monto total de la compra: "))

if monto > 1000:
    monto -= monto * 0.10

print("Monto a pagar:", monto)


# 6. Número positivo, negativo o cero
print("6. Número positivo, negativo o cero")
numero = float(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")


# 7. Día de la semana
print("7. Día de la semana")
dia = int(input("Ingresa un número del 1 al 7: "))

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
