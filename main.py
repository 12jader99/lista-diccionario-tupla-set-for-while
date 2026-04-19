# lista donde se guardaran los estudiantes
estudiantes = []

# tupla con materias disponibles
materias = ("Matemáticas", "Python", "Base de datos", "Inglés")

#Ciclo while: Se utiliza para mantener el menú en ejecución hasta que el usuario decida salir.
while True:
    print("SISTEMA DE REGISTRO DE ESTUDIANTES")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Mostrar materias registradas")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
        except ValueError:
            print("Edad inválida. Debe ser un número.")
            continue

        print("Materias disponibles:")
        for i, mat in enumerate(materias, 1):
            print(f"{i}. {mat}")

        try:
            num_materia = int(input("Seleccione el número de la materia: "))
            if 1 <= num_materia <= len(materias):
                curso = materias[num_materia - 1]
            else:
                print("Número inválido.")
                continue
        except ValueError:
            print("Entrada inválida.")
            continue
# Diccionarios: Cada estudiante se almacena como un diccionario con nombre, edad y materia.
        estudiante = {
            "nombre": nombre,
            "edad": edad,
            "materia": curso
        }

        estudiantes.append(estudiante)
        print("Estudiante registrado exitosamente.")

    elif opcion == "2":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("\nLista de estudiantes registrados:")
            for alumno in estudiantes:
                print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Materia: {alumno['materia']}")

    elif opcion == "3":
        nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
        encontrado = False

#Ciclo for: Se utiliza para recorrer las materias y los estudiantes registrados.
        for alumno in estudiantes:
            if alumno["nombre"].lower() == nombre_buscar.lower():
                print(f"Estudiante encontrado: Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Materia: {alumno['materia']}")
                encontrado = True
                break

        if not encontrado:
            print("Estudiante no encontrado.")

    elif opcion == "4":
        #Sets: Se utiliza un set para mostrar las materias registradas sin repetir.
        materias_registradas = set()

        for alumno in estudiantes:
            materias_registradas.add(alumno["materia"])

        if len(materias_registradas) == 0:
            print("No hay materias registradas.")
        else:
            print("\nMaterias registradas:")
            for materia in materias_registradas:
                print(materia)

    elif opcion == "5":
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")