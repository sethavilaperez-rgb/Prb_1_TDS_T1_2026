# Caso 2: Sistema de Gestión de Inventarios

# --- Clase Producto ---
# Representa un producto del inventario.
# Sus atributos son privados para proteger datos como el precio
# y la cantidad, así solo se modifican a través de métodos.
class Producto:
    # El constructor recibe los datos del producto y los guarda
    def __init__(self, nombre, codigo, precio, cantidad):
        # Atributos PRIVADOS (doble guion bajo __):
        # Protegemos estos datos para que no se cambien directamente
        # desde fuera, solo mediante métodos de la clase.
        self.__nombre = nombre
        self.__codigo = codigo
        self.__precio = precio
        self.__cantidad = cantidad

    # Getters: permiten leer los atributos privados sin modificarlos
    def get_nombre(self):
        return self.__nombre

    def get_codigo(self):
        return self.__codigo

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    # Método para reducir stock al hacer una venta
    def reducir_stock(self, cantidad):
        # Validamos que haya suficiente stock antes de descontar
        if cantidad > self.__cantidad:
            print("No hay suficiente stock disponible.")
            return False
        self.__cantidad -= cantidad
        return True

    # Método para agregar más stock a un producto existente
    def agregar_stock(self, cantidad):
        self.__cantidad += cantidad

    # __str__ define cómo se muestra el producto al imprimirlo
    def __str__(self):
        return f"{self.__nombre} ({self.__codigo}) - ${self.__precio:.2f} | Stock: {self.__cantidad}"


# --- Clase Venta ---
# Representa una venta realizada. Guarda qué producto se vendió,
# cuántas unidades y el total cobrado.
# Sus atributos son públicos porque solo es un registro de datos,
# no necesita protección especial.
class Venta:
    def __init__(self, producto_nombre, producto_codigo, cantidad, precio_unitario):
        self.producto_nombre = producto_nombre
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        # El total se calcula automáticamente al crear la venta
        self.total = cantidad * precio_unitario

    def __str__(self):
        return f"{self.producto_nombre} x{self.cantidad} = ${self.total:.2f}"


# --- Clase SistemaInventario ---
# Clase controladora que coordina productos, ventas y reportes.
# Usa un diccionario para los productos (búsqueda rápida por código)
# y una lista para las ventas (se van acumulando en orden).
class SistemaInventario:
    def __init__(self):
        self.productos = {}   # Diccionario: código -> objeto Producto
        self.ventas = []      # Lista de objetos Venta

    # Registra un nuevo producto verificando que el código no se repita
    def registrar_producto(self, nombre, codigo, precio, cantidad):
        if codigo in self.productos:
            print("Ya existe un producto con ese código.")
            return
        self.productos[codigo] = Producto(nombre, codigo, precio, cantidad)
        print(f"Producto '{nombre}' registrado correctamente.")

    # Realiza una venta validando que el producto exista y tenga stock
    def realizar_venta(self, codigo_producto, cantidad):
        if codigo_producto not in self.productos:
            print("No se encontró el producto.")
            return
        producto = self.productos[codigo_producto]

        # Intentamos reducir el stock, si no hay suficiente retorna False
        if not producto.reducir_stock(cantidad):
            return

        # Creamos el registro de venta y lo guardamos en la lista
        venta = Venta(
            producto.get_nombre(),
            producto.get_codigo(),
            cantidad,
            producto.get_precio()
        )
        self.ventas.append(venta)
        print(f"Venta realizada: {venta}")

    # Suma el total de todas las ventas registradas
    def calcular_total_ventas(self):
        if not self.ventas:
            print("No hay ventas registradas.")
            return 0
        total = sum(v.total for v in self.ventas)
        print(f"\nTotal de ventas: ${total:.2f}")
        print(f"Número de ventas realizadas: {len(self.ventas)}")
        return total

    # Muestra un reporte con todos los productos y su stock actual
    def generar_reporte_inventario(self):
        print("\n--- Reporte de Inventario ---")
        if not self.productos:
            print("No hay productos registrados.")
            return
        print(f"{'Producto':<20} {'Código':<10} {'Precio':<12} {'Stock'}")
        print(f"{'-'*20} {'-'*10} {'-'*12} {'-'*6}")
        for producto in self.productos.values():
            print(f"{producto.get_nombre():<20} {producto.get_codigo():<10} ${producto.get_precio():<11.2f} {producto.get_cantidad()}")

        # También mostramos las ventas si hay
        if self.ventas:
            print(f"\n--- Ventas realizadas ---")
            for i, venta in enumerate(self.ventas, 1):
                print(f"  {i}. {venta}")
            total = sum(v.total for v in self.ventas)
            print(f"  Total acumulado: ${total:.2f}")


# --- Menú interactivo ---
# Función principal que carga datos de prueba y muestra un menú
# para que el usuario interactúe con el sistema.

def menu():
    sistema = SistemaInventario()

    # Datos precargados para pruebas
    sistema.registrar_producto("Laptop", "P001", 15999.99, 10)
    sistema.registrar_producto("Mouse", "P002", 299.50, 50)
    sistema.registrar_producto("Teclado", "P003", 450.00, 30)
    sistema.registrar_producto("Monitor", "P004", 4500.00, 15)
    sistema.registrar_producto("Audífonos", "P005", 850.00, 25)

    sistema.realizar_venta("P001", 2)
    sistema.realizar_venta("P002", 5)
    sistema.realizar_venta("P003", 3)


    # Ciclo del menú: se repite hasta que el usuario elija salir
    while True:
        print("\n===== Sistema de Gestión de Inventarios =====")
        print("1. Registrar producto")
        print("2. Realizar venta")
        print("3. Calcular total de ventas")
        print("4. Generar reporte de inventario")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            codigo = input("Código del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad en stock: "))
            sistema.registrar_producto(nombre, codigo, precio, cantidad)

        elif opcion == "2":
            codigo = input("Código del producto a vender: ")
            cantidad = int(input("Cantidad a vender: "))
            sistema.realizar_venta(codigo, cantidad)

        elif opcion == "3":
            sistema.calcular_total_ventas()

        elif opcion == "4":
            sistema.generar_reporte_inventario()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


# Punto de entrada: solo ejecuta el menú si corremos este archivo directamente
if __name__ == "__main__":
    menu()
