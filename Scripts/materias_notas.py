n_materias = int(input("Ingrese num materias: "))

materias = []
notas = []

for i in range(0, n_materias):
    nombre = input("Ingrese nombre: ")
    materias.append(nombre)

    nota = float(input("ingrese nota: "))
    notas.append(nota)

for j in range(0, n_materias):
    print(f"materia: {materias[j]} - nota: {notas[j]}")