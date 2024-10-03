from core1 import NewFile, ReadFile

def AddData(campo, info):
    """Añade un nuevo camper a la base de datos."""
    data = ReadFile()  # Leer los datos actuales
    if campo not in data.get('campers', {}):
        data.setdefault('campers', {})[campo] = info  # Agrega la nueva información
        NewFile(data)  # Guarda los cambios
        print(f"Camper {campo} añadido.")
    else:
        print(f"El camper {campo} ya existe.")

def DeleteData(campo):
    """Elimina un camper de la base de datos."""
    data = ReadFile()  # Leer los datos actualesz
    if campo in data.get('campers', {}):
        del data['campers'][campo]  # Elimina el camper
        NewFile(data)  # Guarda los cambios
        print(f"Camper {campo} eliminado.")
    else:
        print(f"El camper {campo} no existe.")
        
