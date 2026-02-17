"""
1. Sistema de votaciones electrónicas

Este programa simula una votación escolar sencilla.
La idea es poder registrar candidatos, permitir que los alumnos voten
solo una ves y al final mostrar los resultados con porcentajes
y el ganador

También se valida que la matrícula sea correcta
(que empiece con 2028 y tenga 4 núueros despues).
Si algo no cumple, simplemente no deja votar
"""

#--------------------------------------------------------------------
#Colecciones principales

#Aquí se guardan los candidatos.
#La clave es el ID y el valor es una tupla (nombre, partido).
candidatos = {}

#Aquí se guardan los votos válidos.
#La clave es la matrícula y el valor es el ID del candidato.
votos = {}

#Aquí se guardan las matrículas que hicieron voto nulo.
votos_nulos = []

#--------------------------------------------------
#Registrar candidato


def registrar_candidato():
    """
    Esta función sirve para agregar un candidato al sistema.

    Pide el ID, el nombre y el partido.
    Luego lo guarda en el diccionario.

    Si el ID ya existía, lo reemplaza.
    No hace validación extra porque asumimos que
    quien registra candidatos sabe lo que está haciendo.
    """

    id_candidato = input("Ingresa ID del candidato: ")
    nombre = input("Ingresa nombre del candidato: ")
    partido = input("Ingresa partido del candidato: ")

    candidatos[id_candidato] = (nombre, partido)

    print("Candidato registrado correctamente.\n")

#--------------------------------------------------------
#Validar votante

def validar_voto(matricula):
    """
    Aquí es donde se revisa si el alumno puede votar.

    Se validan cuatro cosas importantes:

    1) Que la matrícula tenga 8 caracteres.
    2) Que empiece con 2028.
    3) Que los últimos 4 sean números.
    4) Que no haya votado antes.

    Si falla alguna, se regresa False.
    Si todo está bien, se regresa True.
    """

    #Primero revisamos que tenga exactamente 8 caracteres.
    if len(matricula) != 8:
        print("Matrícula inválida. Debe tener 8 caracteres.")
        return False

    #Ahora verificamos que empiece con 2028.
    #startswith() revisa cómo inicia el texto.
    if not matricula.startswith("2028"):
        print("Matrícula inválida. Debe comenzar con 2028.")
        return False

    #Aquí revisamos que los últimos 4 caracteres sean números.
    #isdigit() confirma que solo haya dígitos.
    if not matricula[4:].isdigit():
        print("Matrícula inválida. Los últimos 4 deben ser números.")
        return False

    #Finalmente, revisamos que no haya votado antes.
    if matricula in votos or matricula in votos_nulos:
        print("Este alumno ya votó.")
        return False

    #Si paso todo entonces se puede votar
    return True

#------------------------------------------------
#Emitir voto

def emitir_voto():
    """
    Esta función permite votar.

    Hay tres posibles escenarios:

    - Si escribe 0 → es voto nulo.
    - Si escribe un ID que existe → voto válido.
    - Si escribe algo que no existe → también cuenta como nulo.

    Antes de todo eso, se valida la matrícula.
    """

    matricula = input("Ingresa tu matrícula: ")

    # Si la validación falla, simplemente se detiene aquí.
    if not validar_voto(matricula):
        return

    print("\nCandidatos disponibles:")
    for id_candidato, datos in candidatos.items():
        print(f"{id_candidato} - {datos[0]} ({datos[1]})")

    print("0 - Voto Nulo")

    voto = input("Ingresa el ID del candidato: ")

    # Si elige 0, es voto nulo directo.
    if voto == "0":
        votos_nulos.append(matricula)
        print("Has emitido un voto nulo.\n")

    # Si el ID existe dentro del diccionario, es válido.
    elif voto in candidatos:
        votos[matricula] = voto
        print("Voto registrado correctamente.\n")

    # Si no es 0 ni existe el ID, también se toma como nulo.
    else:
        votos_nulos.append(matricula)
        print("ID inválido. Se registró como voto nulo.\n")

#---------------------------------------}
#Contar votos

def contar_votos():
    """
    Aquí se cuentan los votos válidos.

    Primero se crea un diccionario donde todos los candidatos
    empiezan con 0 votos.

    Después se recorren los votos válidos y se va sumando.
    """

    conteo = {id_candidato: 0 for id_candidato in candidatos}

    for voto in votos.values():
        conteo[voto] += 1

    return conteo


#-----------------------------------------------
#Mostrar resultados

def mostrar_resultados():
    """
    Esta parte muestra todo al final:

    - Cuántos votos tiene cada candidato.
    - Qué porcentaje obtuvo.
    - Cuántos votos válidos hubo.
    - Cuántos nulos.
    - Y quién ganó.

    Si nadie ha votado, simplemente avisa y no intenta calcular nada.
    """

    conteo = contar_votos()

    total_validos = len(votos)
    total_nulos = len(votos_nulos)
    total_emitidos = total_validos + total_nulos

    print("\n===== RESULTADOS =====")

    # Esto evita dividir entre cero si nadie votó.
    if total_emitidos == 0:
        print("No hay votos registrados.")
        return

    for id_candidato, cantidad in conteo.items():
        nombre, partido = candidatos[id_candidato]
        porcentaje = (cantidad / total_emitidos) * 100
        print(f"{nombre} ({partido}) - {cantidad} votos ({porcentaje:.2f}%)")

    print("\nEstadísticas generales:")
    print("Votos válidos:", total_validos)
    print("Votos nulos:", total_nulos)
    print("Participación total:", total_emitidos)

    # Aquí se usa max() para obtener el que tenga más votos.
    if conteo:
        ganador = max(conteo, key=conteo.get)
        print("Ganador:", candidatos[ganador][0])


#----------------------------------------------------
#Menu

def menu():
    """
    Este es el control del programa.

    Se repite hasta que el usuario elija salir.
    Básicamente conecta todas las funciones anteriores.
    """

    while True:
        print("\n===== SISTEMA DE VOTACIONES =====")
        print("1. Registrar candidato")
        print("2. Emitir voto")
        print("3. Mostrar resultados")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_candidato()
        elif opcion == "2":
            emitir_voto()
        elif opcion == "3":
            mostrar_resultados()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

# Aquí inicia todo
menu()

