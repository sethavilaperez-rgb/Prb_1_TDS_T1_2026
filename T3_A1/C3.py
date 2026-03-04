# Caso 3: Sistema de Gestión de Tareas

# --- Clase Tarea ---
# Representa una tarea con su información y estado actual.
# Los atributos son privados para controlar que el estado solo
# se cambie mediante el método actualizar_estado, así validamos
# que solo se usen los estados permitidos.
class Tarea:
    # Lista de estados válidos como atributo de clase,
    # porque aplica para TODAS las tareas, no cambia por instancia.
    ESTADOS_VALIDOS = ["pendiente", "en progreso", "completada"]

    # El constructor recibe los datos y pone el estado inicial en "pendiente"
    def __init__(self, titulo, descripcion, fecha_vencimiento):
        # Atributos PRIVADOS (doble guion bajo __):
        # Protegemos los datos para que no se modifiquen directamente,
        # especialmente el estado que debe pasar por validación.
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__fecha_vencimiento = fecha_vencimiento
        self.__estado = "pendiente"  # Toda tarea nueva empieza como pendiente

    # Getters para leer los atributos privados desde fuera
    def get_titulo(self):
        return self.__titulo

    def get_descripcion(self):
        return self.__descripcion

    def get_fecha_vencimiento(self):
        return self.__fecha_vencimiento

    def get_estado(self):
        return self.__estado

    # Método para actualizar el estado validando que sea uno permitido
    def actualizar_estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            print(f"Estado no válido. Los estados permitidos son: {self.ESTADOS_VALIDOS}")
            return False
        self.__estado = nuevo_estado
        print(f"Tarea '{self.__titulo}' actualizada a '{nuevo_estado}'.")
        return True

    # __str__ para mostrar la tarea de forma legible al imprimirla
    def __str__(self):
        return f"[{self.__estado.upper()}] {self.__titulo} - Vence: {self.__fecha_vencimiento}"


# --- Clase SistemaTareas ---
# Clase controladora que administra todas las tareas.
# Usa una lista para guardar las tareas porque el orden
# en que se crean es importante para los reportes.
class SistemaTareas:
    def __init__(self):
        self.tareas = []  # Lista de objetos Tarea

    # Crea una nueva tarea y la agrega a la lista
    def crear_tarea(self, titulo, descripcion, fecha_vencimiento):
        # Verificar que no exista otra tarea con el mismo título
        for t in self.tareas:
            if t.get_titulo() == titulo:
                print("Ya existe una tarea con ese título.")
                return
        tarea = Tarea(titulo, descripcion, fecha_vencimiento)
        self.tareas.append(tarea)
        print(f"Tarea '{titulo}' creada correctamente.")

    # Busca una tarea por título y le cambia el estado
    def actualizar_estado(self, titulo, nuevo_estado):
        for t in self.tareas:
            if t.get_titulo() == titulo:
                t.actualizar_estado(nuevo_estado)
                return
        print("No se encontró una tarea con ese título.")

    # Genera un reporte separando tareas por estado
    def generar_reporte_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return

        # Separamos las tareas por estado usando listas
        pendientes = []
        en_progreso = []
        completadas = []

        for t in self.tareas:
            if t.get_estado() == "pendiente":
                pendientes.append(t)
            elif t.get_estado() == "en progreso":
                en_progreso.append(t)
            elif t.get_estado() == "completada":
                completadas.append(t)

        print("\n--- Reporte de Tareas ---")
        print(f"Total de tareas: {len(self.tareas)}")

        print(f"\nPendientes ({len(pendientes)}):")
        if pendientes:
            for t in pendientes:
                print(f"  - {t.get_titulo()} | {t.get_descripcion()} | Vence: {t.get_fecha_vencimiento()}")
        else:
            print("  No hay tareas pendientes.")

        print(f"\nEn progreso ({len(en_progreso)}):")
        if en_progreso:
            for t in en_progreso:
                print(f"  - {t.get_titulo()} | {t.get_descripcion()} | Vence: {t.get_fecha_vencimiento()}")
        else:
            print("  No hay tareas en progreso.")

        print(f"\nCompletadas ({len(completadas)}):")
        if completadas:
            for t in completadas:
                print(f"  - {t.get_titulo()} | {t.get_descripcion()} | Vence: {t.get_fecha_vencimiento()}")
        else:
            print("  No hay tareas completadas.")


# --- Menú interactivo ---
# Función principal que carga datos de prueba y muestra un menú
# para que el usuario interactúe con el sistema.

def menu():
    sistema = SistemaTareas()

    # Datos precargados para pruebas
    sistema.crear_tarea("Entregar proyecto", "Subir el proyecto final de POO", "2026-03-10")
    sistema.crear_tarea("Estudiar para examen", "Repasar temas de bases de datos", "2026-03-15")
    sistema.crear_tarea("Hacer ejercicios", "Resolver los 5 ejercicios de cálculo", "2026-03-08")
    sistema.crear_tarea("Leer artículo", "Leer el paper de inteligencia artificial", "2026-03-12")
    sistema.crear_tarea("Presentación", "Preparar las diapositivas de redes", "2026-03-20")

    sistema.actualizar_estado("Entregar proyecto", "en progreso")
    sistema.actualizar_estado("Hacer ejercicios", "completada")


    # Ciclo del menú: se repite hasta que el usuario elija salir
    while True:
        print("\n===== Sistema de Gestión de Tareas =====")
        print("1. Crear tarea")
        print("2. Actualizar estado de tarea")
        print("3. Generar reporte de tareas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción: ")
            fecha = input("Fecha de vencimiento (AAAA-MM-DD): ")
            sistema.crear_tarea(titulo, descripcion, fecha)

        elif opcion == "2":
            titulo = input("Título de la tarea: ")
            print("Estados disponibles: pendiente, en progreso, completada")
            nuevo_estado = input("Nuevo estado: ")
            sistema.actualizar_estado(titulo, nuevo_estado)

        elif opcion == "3":
            sistema.generar_reporte_tareas()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


# Punto de entrada: solo ejecuta el menú si corremos este archivo directamente
if __name__ == "__main__":
    menu()
