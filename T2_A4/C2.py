from datetime import datetime

"""
2. Gestor de Reservas de un Cine

Este programa simula el sistema de reservas de un cine.

Permite:
- Ver el mapa de asientos (8 filas x 10 columnas).
- Reservar un asiento indicando fila y columna.
- Validar que el asiento no esté ocupado.
- Calcular el precio dependiendo la zona.
- Guardar un historial de todas las reservas hechas.

La idea es aplicar matrices, diccionarios y listas de tuplas
de forma práctica.
"""

#----------------------------------------------------
#Colecciones princpales

# Creamos la sala como una matriz 8x10
#Cada asiento inicia con "O" (Disponible).
sala = [["O" for _ in range(10)] for _ in range(8)]

#Diccionario de precios por zona.
#Las filas 0-2 serán zona VIP
#Las filas 3-5 zona Preferente
#Las filas 6-7 zona General
precios = {
    "VIP": 120,
    "Preferente": 80,
    "General": 50
}

# Lista para guardar historial de reservas.
#Cada elemento será una tupla:
#(fila, columna, precio, hora)
historial = []

#---------------------------------
#Mostrar sala

def mostrar_sala():
    """
    Muestra el mapa actual de la sala.

    O = Disponible
    X = Ocupado

    Se muestran números de fila y columna
    para que sea más fácil elegir asiento.
    """

    print("\n===== MAPA DE ASIENTOS =====")

    #Imprime encabezado de columnas
    print("   ", end="")
    for col in range(10):
        print(col, end=" ")
    print()

    # Recorremos cada fila de la matriz
    for i, fila in enumerate(sala):
        print(i, end="  ")
        for asiento in fila:
            print(asiento, end=" ")
        print()


#----------------------------------------------------
#Calcular precio

def calcular_precio(fila):
    """
    Determina el precio dependiendo la fila.

    Condiciones:
    - Si la fila está entre 0 y 2 es VIP
    - Si está entre 3 y 5 es Preferente
    - Si está entre 6 y 7 es General

    Se usa comparación con rangos para decidir la zona.
    """

    if 0 <= fila <= 2:
        return precios["VIP"]

    elif 3 <= fila <= 5:
        return precios["Preferente"]

    elif 6 <= fila <= 7:
        return precios["General"]

    else:
        #Esto solo pasaría si la fila no es válida
        return None

#--------------------------------------------------------------
#Reservar asiento

def reservar_asiento(fila, columna):
    """
    Intenta reservar un asiento específico.

    Validaciones importantes:
    1) Que la fila esté dentro del rango (0-7).
    2) Que la columna esté dentro del rango (0-9).
    3) Que el asiento no esté ocupado.

    Si todo está correcto:
    - Marca el asiento como "X".
    - Calcula el precio.
    - Guarda la reserva en el historial.
    """

    #Validamos que la fila esté dentro del rango.
    #Esto evita errores como intentar acceder a una posición que no existe.
    if fila < 0 or fila > 7:
        print("Fila inválida.")
        return

    #Validamos columna.
    if columna < 0 or columna > 9:
        print("Columna inválida.")
        return

    #Revisamos si el asiento ya está ocupado.
    #Si en la matriz ya aparece "X", significa que alguien ya lo reservó
    if sala[fila][columna] == "X":
        print("Ese asiento ya está ocupado.")
        return

    # Si paso todas las validaciones, entonces se puede reservar.
    sala[fila][columna] = "X"

    precio = calcular_precio(fila)
    hora = datetime.now().strftime("%H:%M:%S")

    historial.append((fila, columna, precio, hora))

    print(f"Asiento reservado correctamente. Precio: ${precio}")

#-----------------------------------------------------------
#Generar reporte

def generar_reporte():
    """
    Muestra un resumen de todas las reservas realizadas.

    Incluye:
    - Fila
    - Columna
    - Precio pagado
    - Hora de la reserva
    - Total recaudado

    Si no hay reservas, simplemente lo indica.
    """

    print("\n===== REPORTE DE RESERVAS =====")

    if not historial:
        print("No hay reservas registradas.")
        return

    total = 0

    for reserva in historial:
        fila, columna, precio, hora = reserva
        print(f"Fila {fila}, Columna {columna} | ${precio} | Hora: {hora}")
        total += precio

    print("\nTotal recaudado: $", total)

#-----------------------------------------------------
#Menu

def menu():
    """
    Controla todo el sistema.

    Permite:
    1) Ver la sala
    2) Reservar asiento
    3) Ver reporte
    4) Salir

    Se usa un ciclo infinito que solo se rompe
    cuando el usuario elige salir.
    """

    while True:
        print("\n===== CINE =====")
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Generar reporte")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_sala()

        elif opcion == "2":
            try:
                fila = int(input("Ingresa fila (0-7): "))
                columna = int(input("Ingresa columna (0-9): "))
                reservar_asiento(fila, columna)
            except ValueError:
                # Esto evita que el programa se rompa
                # si el usuario escribe algo que no sea número.
                print("Debes ingresar números válidos.")

        elif opcion == "3":
            generar_reporte()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

# Aquí inicia el programa
menu()
