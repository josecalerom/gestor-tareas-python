"""En primer lugar, se importó la librería sys para que no existan problemas con caracteres
propios del español durante la ejecución de código"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

class Tarea:
    def __init__(self, descripcion, completada=False):
        """Constructor de la clase Tarea, inicializa una tarea con una descripción y
        el estado de completado (opcional)."""
        self.descripcion = descripcion
        self.completada = completada

class GestorTareas:
    def __init__(self):
        """Constructor de la clase GestorTareas, inicializa una lista vacía de tareas."""
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """Método para agregar una nueva tarea a la lista de tareas."""
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def marcar_completada(self, posicion):
        """Método para marcar una tarea como completada dado su posición en la lista."""
        if 0 <= posicion < len(self.tareas):
            self.tareas[posicion].completada = True
        else:
            raise IndexError("La posición ingresada no es válida.")

    def mostrar_tareas(self):
        """Método para imprimir todas las tareas pendientes en la lista."""
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{i + 1}. [{estado}] {tarea.descripcion}")

    def eliminar_tarea(self, posicion):
        """Método para eliminar una tarea de la lista, solicitando confirmación al usuario."""
        if 0 <= posicion < len(self.tareas):
            while True:
                confirmacion = input(f"¿Está seguro que desea eliminar la tarea '{self.tareas[posicion].descripcion}'? (s/n): ").lower()
                if confirmacion in {'s', 'si', 'sí'}:
                    del self.tareas[posicion]
                    break
                elif confirmacion in {'n', 'no'}:
                    print("Acción cancelada.")
                    break
                else:
                    print("Opción no válida. Por favor, ingrese 's' para eliminar o 'n' para cancelar.")
        else:
            raise IndexError("El índice que ingresaste no es válido.")

if __name__ == "__main__":
    gestor = GestorTareas()

    while True:
        print("\n--- Programa de gestión de Tareas ---")
        # Menú que muestra las opciones disponibles para el usuario interactúe con el programa de gestión de tareas.
        print("1. Agrega una tarea nueva")
        print("2. Marca como completada una tarea existente (dado el índice)")
        print("3. Muestra todas las tareas registradas")
        print("4. Elimina una tarea (dado el índice)")
        print("5. Salir de la ejecución del programa")

        opcion = input("Por favor, ingresa el número de la opción que deseas ejecutar: ")

        if opcion == "1":
            descripcion = input("Por favor, ingresa la descripción de la nueva tarea: ")
            gestor.agregar_tarea(descripcion)
        elif opcion == "2":
            try:
                posicion = int(input("Por favor, ingresa el índice de la tarea que deseas marcar como completada: ")) - 1
                gestor.marcar_completada(posicion)
            except (ValueError, IndexError) as e:
                print("Error:", e)
        elif opcion == "3":
            gestor.mostrar_tareas()
        elif opcion == "4":
            try:
                posicion = int(input("Por favor, ingresa el índice de la tarea que deseas eliminar: ")) - 1
                gestor.eliminar_tarea(posicion)
            except (ValueError, IndexError) as e:
                print("Error:", e)
        elif opcion == "5":
            print("Programa terminado. ¡Adiós!")
            break
        else:
            print("La opción seleccionada es inválida. Por favor, ingresa un número del 1 al 5.")
