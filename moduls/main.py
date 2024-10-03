import os
import sys
import json
from core1 import CheckFile, ReadFile
from custom import AddData, DeleteData

def borrar_pantalla():
    """Limpia la consola."""
    os.system("cls" if os.name == "nt" else "clear")

def pausar_pantalla():
    """Pausa la ejecución y espera a que el usuario presione una tecla."""
    input("Presione una tecla para continuar...")

if __name__ == '__main__':
    campus = {'campers': {}}
    CheckFile(campus)  # Verifica y crea el archivo si no existe
    print("Bienvenido al sistema de gestión de campers")

    # Ejemplo de uso
    while True:
        borrar_pantalla()
        print("1. Añadir Camper")
        print("2. Eliminar Camper")
        print("3. Ver Campers")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del camper: ")
            info = input("Ingrese información del camper (en formato JSON): ")
            try:
                info = json.loads(info)  # Convierte la cadena en un diccionario
                AddData(nombre, info)  # Añade el camper
            except json.JSONDecodeError:
                print("Error: Información inválida.")
        elif opcion == '2':
            nombre = input("Ingrese el nombre del camper a eliminar: ")
            DeleteData(nombre)  # Elimina el camper
        elif opcion == '3':
            data = ReadFile()  # Lee los campers
            print(json.dumps(data, indent=4))  # Muestra la información de los campers
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")
        
        pausar_pantalla()
