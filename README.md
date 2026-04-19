Sistema de Registro de Estudiantes

Este proyecto es una aplicación desarrollada en Python que permite registrar estudiantes, consultar la lista de estudiantes, buscar estudiantes por nombre y mostrar las materias registradas.

El programa fue desarrollado en un único archivo llamado main.py, usando las estructuras vistas en clase: listas, diccionarios, tuplas, sets y ciclos for y while.

Cómo ejecutar el programa

1. Abrir la terminal en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

bash
python main.py


Funcionalidades

Agregar estudiantes
Mostrar estudiantes registrados
Buscar estudiantes por nombre
Mostrar materias registradas sin repetir

Estructuras utilizadas

Listas

Se utiliza una lista llamada "estudiantes" para guardar todos los estudiantes registrados.

estudiantes = []

Diccionarios

Cada estudiante se almacena como un diccionario con nombre, edad y materia.

estudiante = {
    "nombre": nombre,
    "edad": edad,
    "materia": curso
}

Tuplas

Las materias disponibles se guardan en una tupla.

materias = ("Matemáticas", "Python", "Base de datos", "Inglés")

Sets

Se utiliza un set para mostrar las materias registradas sin repetir.

materias_registradas = set()

Ciclo while

Se utiliza para mantener el menú en ejecución hasta que el usuario decida salir.

while True:

Ciclo for

Se utiliza para recorrer las materias y los estudiantes registrado

for alumno in estudiantes:

