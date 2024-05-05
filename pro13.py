def mostrar_estudiantes(estudiantes):
    print("Lista de estudiante: ")
    if estudiantes:
        for estudiante in estudiantes:
            print("-", estudiante)
    else:
        print("No hay estudiante registrado.")
def buscar_estudiante(estudiantes, nombre):
    for estudiante in estudiantes:
        if estudiante.lower() == nombre.lower():
            return True
        return False
estudiantes = []
while True:
    print('''
          1-Agregar estudiante
          2-Mostrar lsita de estudiantes
          3-Buscar estudiante por nombre
          4-Eliminar estudiante
          5-Salir
          ''')
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        nombre_estudiante = input("Ingresar el nombre: ")
        estudiantes.append(nombre_estudiante)
        print("Estudiante agregado.")
    elif opcion == 2:
        mostrar_estudiantes(estudiantes)
    elif opcion == 3:
        nombre_buscar = input("Ingrese el nombre a buscar: ")
        if buscar_estudiante(estudiantes, nombre_estudiante):
            print("El estudiante esta en la lista.")
        else:
            print("El estudiante no esta en la lista.")
    elif opcion == 4:
        nombre_eliminar = input("Ingresa el nombre a eliminar: ")
        if buscar_estudiante(estudiantes,nombre_estudiante):
            estudiantes.remove(nombre_eliminar)
            print("Eliminado exitosamente.")
        else:
            print("El estudiante no esta en la lista.")
    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("Vueleve a intentarlo.")