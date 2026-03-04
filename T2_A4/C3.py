"""
3. Sistema de Gestión de Biblioteca

Este sistema simula el funcionamiento básico de una biblioteca.

- Permite registrar libros.
- Permite prestar libros validando disponibilidad.
- Gestiona devoluciones y calcula multas si hay retraso.
- Genera reportes útiles.
- Recomienda libros según historial del usuario.

Se usara:
- Lista de diccionarios para almacenar libros.
- Diccionario para préstamos activos.
- Conjunto (set) para géneros sin repetir.
- Lista para historial de préstamos.

"""

from datetime import datetime, timedelta

#---------------------------------------------------
#Colecciones principales

#Aquí guardamos todos los libros.
#Cada libro es un diccionario con sus datos.
libros = []

#Diccionario que guarda préstamos activos.
#Formato:
#{ ISBN : (usuario, fecha_prestamo, fecha_vencimiento) }
prestamos = {}

#Conjunto para generos.
#Usamos set porque automaticamente evita duplicados.
generos = set()

#Historial general de prestamos.
#Nos sirve para estadísticas y recomendaciones.
historial_prestamos = []


#-------------------------------------------------------
#Registrar libro

def registrar_libro():
    """
    Registra un libro en el sistema.

    Aquí simplemente pedimos los datos,
    creamos un diccionario y lo agregamos a la lista.

    También agregamos el género al set,
    porque un set no permite repetidos.
    """

    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    genero = input("Género: ")

    libro = {
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "genero": genero,
        "disponible": True,  # Por defecto siempre inicia disponible
        "veces_prestado": 0  # Nos ayuda para estadísticas
    }

    libros.append(libro)
    generos.add(genero)

    print("Libro registrado correctamente.\n")


#------------------------------------------------------------
#Buscar libro

def buscar_libro(criterio, valor):
    """
    Busca libros por titulo, autor o ISBN.

    La logica aquí es sencilla:
    - Recorremos toda la lista de libros.
    - Comparamos el criterio elegido.
    - Si coincide, lo guardamos en resultados.

    La condición importante:
    if str(libro[criterio]).lower() == valor.lower()

    Convertimos a minúsculas para evitar errores
    si el usuario escribe diferente combinación de mayúsculas.
    """

    resultados = []

    for libro in libros:

        #Condición principal de búsqueda
        if str(libro[criterio]).lower() == valor.lower():
            resultados.append(libro)

    return resultados

#------------------------------------------------------------
#Prestar libro


def prestar_libro(isbn, usuario):
    """
    Permite prestar un libro si está disponible.

    Lógica:
    1. Buscar el libro por ISBN.
    2. Verificar si está disponible.
    3. Si NO está disponible entonces no se presta.
    4. Si está disponible entonces se registra préstamo.
    """

    for libro in libros:

        #Primero validamos que el ISBN coincida
        if libro["isbn"] == isbn:

            #Segunda validación importante:
            #Si el libro NO está disponible, no permitimos préstamo.
            if libro["disponible"] == False:
                print("El libro no está disponible.\n")
                return  #Salimos de la función

            #Si llega aquí significa que SÍ está disponible
            fecha_prestamo = datetime.now()
            fecha_vencimiento = fecha_prestamo + timedelta(days=7)

            prestamos[isbn] = (usuario, fecha_prestamo, fecha_vencimiento)

            libro["disponible"] = False
            libro["veces_prestado"] += 1

            historial_prestamos.append((isbn, usuario))

            print("Préstamo realizado correctamente.")
            print("Fecha límite:", fecha_vencimiento.date(), "\n")
            return

    #Si termina el for y no encontró ISBN
    print("Libro no encontrado.\n")

#----------------------------------------------------------------
#Devolver libro

def devolver_libro(isbn):
    """
    Gestiona la devolución de un libro.

    Primera condición importante:
    if isbn not in prestamos

    Esto significa que el libro NO está registrado como prestado.
    Entonces no podemos devolver algo que no está prestado.
    """

    #Validación clave
    if isbn not in prestamos:
        print("Este libro no está prestado.\n")
        return

    usuario, fecha_prestamo, fecha_vencimiento = prestamos[isbn]

    multa = calcular_multa(fecha_vencimiento)

    # Ahora lo marcamos como disponible otra vez
    for libro in libros:
        if libro["isbn"] == isbn:
            libro["disponible"] = True
            break

    # Eliminamos del diccionario de préstamos
    del prestamos[isbn]

    print("Libro devuelto correctamente.")

    # Condición para multa
    if multa > 0:
        print(f"Tienes una multa de ${multa}\n")
    else:
        print("No hay multa.\n")

#-------------------------------------------------------------------------
#Calcular multa

def calcular_multa(fecha_vencimiento):
    """
    Calcula multa si hay retraso.

    Condición clave:
    if hoy > fecha_vencimiento

    Si la fecha actual es mayor,
    significa que ya pasó el límite.

    Se cobra $10 por día de retraso.
    """

    hoy = datetime.now()

    if hoy > fecha_vencimiento:
        dias_retraso = (hoy - fecha_vencimiento).days
        return dias_retraso * 10

    # Si no hay retraso, multa es 0
    return 0

#-----------------------------------------------
#Recomendar libros

def recomendar_libros(usuario):
    """
    Recomienda libros según el historial del usuario.

    Logica:
    - Buscamos qué libros ha pedido.
    - Detectamos los géneros.
    - Mostramos libros disponibles de esos géneros.
    """

    generos_usuario = set()

    # Buscar historial del usuario
    for isbn, user in historial_prestamos:
        if user == usuario:
            for libro in libros:
                if libro["isbn"] == isbn:
                    generos_usuario.add(libro["genero"])

    print("Recomendaciones para ti:")

    for libro in libros:
        # Dos condiciones al mismo tiempo:
        # 1. Que el género coincida
        # 2. Que esté disponible
        if libro["genero"] in generos_usuario and libro["disponible"]:
            print("-", libro["titulo"])

    print()


#-------------------------------------------------------
#Generar reportes

def generar_reportes():
    """
    Genera 3 reportes importantes:

    1. Libros más prestados
    2. Libros disponibles por género
    3. Usuarios con préstamos vencidos

    Aquí usamos varias condiciones para filtrar información.
    """

    print("\n--- Libros más prestados ---")

    ordenados = sorted(libros, key=lambda x: x["veces_prestado"], reverse=True)

    for libro in ordenados:
        print(libro["titulo"], "-", libro["veces_prestado"], "préstamos")

    print("\n--- Libros disponibles por género ---")

    for genero in generos:
        print(f"\nGénero: {genero}")
        for libro in libros:
            # Dos condiciones:
            # Que coincida el género
            # Que esté disponible
            if libro["genero"] == genero and libro["disponible"]:
                print("-", libro["titulo"])

    print("\n--- Usuarios con préstamos vencidos ---")

    hoy = datetime.now()

    for isbn, (usuario, _, fecha_vencimiento) in prestamos.items():
        # Si la fecha actual supera la fecha límite → está vencido
        if hoy > fecha_vencimiento:
            print(f"Usuario: {usuario} tiene vencido el libro {isbn}")

    print()


# -------------------------------------------------
# Menu

def menu():
    """
    Menú principal del sistema.

    Aquí usamos estructura if-elif-else
    para decidir qué función ejecutar según la opción.
    """

    while True:

        print("1. Registrar libro")
        print("2. Buscar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Recomendar libros")
        print("6. Generar reportes")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_libro()

        elif opcion == "2":
            criterio = input("Buscar por (titulo/autor/isbn): ")
            valor = input("Valor: ")
            resultados = buscar_libro(criterio, valor)
            for libro in resultados:
                print(libro)
            print()

        elif opcion == "3":
            isbn = input("ISBN: ")
            usuario = input("Usuario: ")
            prestar_libro(isbn, usuario)

        elif opcion == "4":
            isbn = input("ISBN: ")
            devolver_libro(isbn)

        elif opcion == "5":
            usuario = input("Usuario: ")
            recomendar_libros(usuario)

        elif opcion == "6":
            generar_reportes()

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            # Esta condición se ejecuta si el usuario
            # escribe algo que no está en las opciones
            print("Opción inválida.\n")


# Ejecutar sistema, donde todo inicia
menu()


