#----1.	Crear una lista
print("----1. Crear una lista")

#Creación de la lista
frutas = ["Sandia", "Pera", "Melon", "Uvas", "Mango"]

#Impresión de la lista completa
print("Lista completa:", frutas)

#Acceso a la posición 3 de la lista, esta empieza en 0
print("Tercer elemento:", frutas[2] + "\n")


#----2.	Modificar una lista
print("----2. Modificar una lista")

#Agregar las 2 frutas a la lista con el metodo append,
#estas se agregaran al final de la lista
frutas.append("Caña")
frutas.append("Mandarina")

# Eliminar la segunda fruta
frutas.pop(1)

print("Lista actualizada:", frutas , "\n")


#----3.	Ordenar una lista
print("----3. Ordenar una lista")

#Creación de la lista de numeros
numeros = [21, 672, 76, 23, 4, 78, 34, 5, 10, 65]

#Metodo que ordena la lista de numero de manera ascendente
numeros.sort()

#Impresión de la lista
print("Lista ordenada:", numeros, "\n")

#----4.	Crear una tupla
print("----4. Crear una tupla")

#Tupla con los días de la semana entre parentesis (sintaxis de la tupla)
dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")

#Impresión de la tupla
print("Tupla completa:", dias)

#Impresión del primer dia de la semana por orden de la tupla declarada
print("Primer día:", dias[0] + "\n")

#----5.	Inmutabilidad de tuplas
print("----5. Inmutabilidad de tuplas")

""" Tratar de modificar la posición 0 de la tupla
Esto dara error debido a que las tuplas son inmutables, lo que quiere decir que 
sus elementos buscan no tener cambios de contenido y orden
"""
#dias[0] = "ERROR"

print()

#----6.	Convertir entre listas y tuplas
print("----6. Convertir entre listas y tuplas")

#Creación de la lista
colores = ["Verde", "Rosa", "Azul", "Morado"]

#con el metodo tuple transformamos la lista en tupla
tupla_colores = tuple(colores)

#Impresión de la tupla
print("Tupla:", tupla_colores)

#Con el metodo list transformamos la tupla anteriormente declarada en lista
lista_colores = list(tupla_colores)

#Impresión de la lista
print("Lista nuevamente:", lista_colores, "\n")

#----7.	Recorrer una lista
print("----7. Recorrer una lista")

#Creación de lista con  ciudades de Mexico
ciudades = ["Toluca", "CDMX", "Guadalajara", "Monterrey", "Puebla"]

"""El metodo for nos permite recorrer la lista a traves de una variable de control
que hace referencia a los elementos dentro de una lista, en este caso imprimira
los elementos de la lista con salto de linea
"""
for ciudad in ciudades:
    print(ciudad)

print()

#----8.	Contar elementos en una lista
print("----8. Contar elementos en una lista")

#Creación de una lista de numeros
numeros = [2, 5, 3, 2, 8, 2, 9, 5, 5, 2, 6, 6, 8, 2]

#con el metodo count y como parametro el número a buscar podemos saber el numero
#de veces que un número aparece en la lista
num = numeros.count(2)

#impresión del numero
print("El número 2 aparece", num, "veces \n")


#----9. Slicing de listas
print("----9. Slicing de listas")

#lista de numeros del 1 al 10
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros, "\n")

#a la variable sublista asignamos el slicing de numeros de nuestra posión 0 a la 5,
#lo que nos dara un total de 5 elementos
sublista = numeros[0:5]

#impresión de la lista
print("Sublista:", sublista, "\n")

#----10. Unir listas
print("----10. Unir listas")

#Creación de una lista de lestras y una lista de numeros
lista1 = ["A", "B", "C"]
lista2 = [1, 2, 3]

#las listas se pueden sumar y modificar su tamaño, a comparación de las tuplas
#pero consumen mas recursos
lista_unida = lista1 + lista2

#impresión de la lista
print("Lista unida:", lista_unida, "\n")

#----11. Desempaquetado de tuplas
print("----11. Desempaquetado de tuplas")

#creación de la tupla
datos = ("Seth", 23, "Toluca")

#python puede guardar para cada variable y en base a la posición del contenido dentro de la tupla
#un valor de dichas variables para despues asignarse o imprimirse o usare
nombre, edad, ciudad = datos

print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)










