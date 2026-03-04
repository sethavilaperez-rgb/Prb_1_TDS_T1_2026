# Caso 1: Sistema de Gestión de Estudiantes

# --- Clase Curso ---
# Representa un curso con su información básica.
# Sus atributos son públicos porque cualquier parte del programa
# necesita acceder al nombre, código y créditos sin restricción.
class Curso:
    # El constructor __init__ se ejecuta al crear un objeto Curso.
    # Recibe los datos del curso y los guarda como atributos de instancia.
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre      # Atributo público
        self.codigo = codigo      # Atributo público
        self.creditos = creditos  # Atributo público

    # __str__ define cómo se muestra el objeto al imprimirlo con print()
    def __str__(self):
        return f"{self.nombre} ({self.codigo}) - {self.creditos} créditos"


# --- Clase Estudiante ---
# Modela a un estudiante con sus datos personales y académicos.
# Los datos personales se manejan como atributos privados (__) para
# que no se puedan modificar directamente desde fuera de la clase,
# solo se leen a través de los getters.
class Estudiante:
    def __init__(self, nombre, matricula, carrera):
        # Atributos PRIVADOS (doble guión bajo __):
        # Se usan para proteger datos sensibles del estudiante.
        # Python les aplica "name mangling", es decir, no se pueden
        # acceder directamente como estudiante.__nombre desde fuera.
        self.__nombre = nombre
        self.__matricula = matricula
        self.__carrera = carrera

        # Atributos PÚBLICOS:
        # cursos_inscritos -> lista porque necesitamos guardar varios cursos en orden
        # calificaciones -> diccionario para asociar cada código de curso con su nota
        self.cursos_inscritos = []
        self.calificaciones = {}

    # Getters: métodos que nos permiten leer los atributos privados
    # sin poder modificarlos desde fuera de la clase
    def get_nombre(self):
        return self.__nombre

    def get_matricula(self):
        return self.__matricula

    def get_carrera(self):
        return self.__carrera

    # Método para inscribir al estudiante en un curso
    def inscribir_curso(self, curso):
        # Validación: máximo 5 cursos por estudiante
        if len(self.cursos_inscritos) >= 5:
            print("No se puede inscribir, ya tiene 5 cursos.")
            return False
        # Validación: que no se repita el mismo curso
        for c in self.cursos_inscritos:
            if c.codigo == curso.codigo:
                print("Ya está inscrito en ese curso.")
                return False
        # Si pasa las validaciones, lo agregamos a la lista
        self.cursos_inscritos.append(curso)
        return True

    # Método para asignar calificación a un curso
    def asignar_calificacion(self, codigo_curso, calificacion):
        # Recorremos los cursos inscritos para verificar que el curso exista
        for c in self.cursos_inscritos:
            if c.codigo == codigo_curso:
                # Guardamos la calificación en el diccionario con el código como llave
                self.calificaciones[codigo_curso] = calificacion
                return True
        print("El estudiante no está inscrito en ese curso.")
        return False

    # Método para calcular el promedio de calificaciones
    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        # sum() suma todas las calificaciones, len() cuenta cuántas hay
        return sum(self.calificaciones.values()) / len(self.calificaciones)

    # Método para mostrar toda la info académica del estudiante
    def mostrar_historial(self):
        print(f"\n--- Historial de {self.__nombre} ---")
        print(f"Matrícula: {self.__matricula}")
        print(f"Carrera: {self.__carrera}")
        print("Cursos inscritos:")
        for curso in self.cursos_inscritos:
            # .get() busca en el diccionario, si no encuentra pone "Sin calificación"
            calif = self.calificaciones.get(curso.codigo, "Sin calificación")
            print(f"  - {curso.nombre} ({curso.codigo}): {calif}")
        print(f"Promedio: {self.calcular_promedio():.2f}")


# --- Clase SistemaGestion ---
# Es la clase "controladora" que coordina todo el sistema.
# Usa un diccionario para guardar estudiantes con su matrícula como llave,
# así podemos buscar a cualquier estudiante de forma directa.
class SistemaGestion:
    def __init__(self):
        self.estudiantes = {}  # Diccionario: matrícula -> objeto Estudiante

    # Registra un nuevo estudiante verificando que la matrícula no se repita
    def registrar_estudiante(self, nombre, matricula, carrera):
        if matricula in self.estudiantes:
            print("Ya existe un estudiante con esa matrícula.")
            return
        self.estudiantes[matricula] = Estudiante(nombre, matricula, carrera)
        print(f"Estudiante '{nombre}' registrado correctamente.")

    # Inscribe a un estudiante en un curso usando su matrícula
    def inscribir_curso(self, matricula, curso):
        if matricula not in self.estudiantes:
            print("No se encontró al estudiante.")
            return
        est = self.estudiantes[matricula]
        if est.inscribir_curso(curso):
            print(f"Curso '{curso.nombre}' inscrito correctamente.")

    # Asigna calificación a un estudiante en un curso específico
    def asignar_calificacion(self, matricula, codigo_curso, calificacion):
        if matricula not in self.estudiantes:
            print("No se encontró al estudiante.")
            return
        self.estudiantes[matricula].asignar_calificacion(codigo_curso, calificacion)

    # Calcula y muestra el promedio del estudiante
    def calcular_promedio(self, matricula):
        if matricula not in self.estudiantes:
            print("No se encontró al estudiante.")
            return
        est = self.estudiantes[matricula]
        print(f"Promedio de {est.get_nombre()}: {est.calcular_promedio():.2f}")

    # Muestra el historial académico completo
    def mostrar_historial(self, matricula):
        if matricula not in self.estudiantes:
            print("No se encontró al estudiante.")
            return
        self.estudiantes[matricula].mostrar_historial()


# --- Menú interactivo ---
# Función principal que carga datos de prueba y muestra un menú
# para que el usuario interactúe con el sistema.

def menu():
    sistema = SistemaGestion()
    cursos_disponibles = {}

    # Datos precargados para pruebas
    cursos_disponibles["0001"] = Curso("Programación", "0001", 6)
    cursos_disponibles["0002"] = Curso("Bases de Datos", "0002", 5)
    cursos_disponibles["0003"] = Curso("Cálculo", "0003", 5)
    cursos_disponibles["0004"] = Curso("Estadística", "0004", 4)
    cursos_disponibles["0005"] = Curso("IA", "0005", 5)
    cursos_disponibles["0006"] = Curso("Fisica", "0006", 4)

    sistema.registrar_estudiante("Seth Avila", "20280780", "Ingenieria en Sistemas")

    sistema.inscribir_curso("20280780", cursos_disponibles["0001"])
    sistema.inscribir_curso("20280780", cursos_disponibles["0002"])
    sistema.inscribir_curso("20280780", cursos_disponibles["0003"])
    sistema.inscribir_curso("20280780", cursos_disponibles["0004"])
    sistema.inscribir_curso("20280780", cursos_disponibles["0005"])

    sistema.asignar_calificacion("20280780", "0001", 90)
    sistema.asignar_calificacion("20280780", "0002", 85)
    sistema.asignar_calificacion("20280780", "0003", 95)
    sistema.asignar_calificacion("20280780", "0004", 78)
    sistema.asignar_calificacion("20280780", "0005", 90)

    # Ciclo del menú: se repite hasta que el usuario elija salir
    while True:
        print("\n===== Sistema de Gestión de Estudiantes =====")
        print("1. Registrar estudiante")
        print("2. Crear curso")
        print("3. Inscribir curso a estudiante")
        print("4. Asignar calificación")
        print("5. Calcular promedio")
        print("6. Mostrar historial académico")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            matricula = input("Matrícula: ")
            carrera = input("Carrera: ")
            sistema.registrar_estudiante(nombre, matricula, carrera)

        elif opcion == "2":
            nombre = input("Nombre del curso: ")
            codigo = input("Código del curso: ")
            creditos = int(input("Créditos: "))
            cursos_disponibles[codigo] = Curso(nombre, codigo, creditos)
            print(f"Curso '{nombre}' creado correctamente.")

        elif opcion == "3":
            matricula = input("Matrícula del estudiante: ")
            codigo = input("Código del curso a inscribir: ")
            if codigo not in cursos_disponibles:
                print("Ese curso no existe, créalo primero.")
            else:
                sistema.inscribir_curso(matricula, cursos_disponibles[codigo])

        elif opcion == "4":
            matricula = input("Matrícula del estudiante: ")
            codigo = input("Código del curso: ")
            calificacion = float(input("Calificación: "))
            sistema.asignar_calificacion(matricula, codigo, calificacion)

        elif opcion == "5":
            matricula = input("Matrícula del estudiante: ")
            sistema.calcular_promedio(matricula)

        elif opcion == "6":
            matricula = input("Matrícula del estudiante: ")
            sistema.mostrar_historial(matricula)

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


# Punto de entrada: solo ejecuta el menú si corremos este archivo directamente
if __name__ == "__main__":
    menu()
