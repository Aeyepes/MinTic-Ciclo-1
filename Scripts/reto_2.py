# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

# NO MODIFICAR EL NOMBRE, PARÁMETROS O RETORNO DE LA FUNCIÓN
def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN modificar_materia (En este espacio debes 
    # poner el código necesario para implementar esta funcionalidad)
    if (0 < semestre <= len(pensum)) == False:
        mensaje = "Ingrese un semestre válido"
    elif len(pensum[semestre - 1]) == 0:
        mensaje = "El semestre no tiene materias"
    elif pensum[semestre - 1].get(materia) == None:
        mensaje = "La materia no existe"
    else:
        mensaje = "Modificada con éxito"
        pensum[semestre - 1][materia] = {'nombre': nombre,'créditos': creditos}    
    # ACÁ TERMINA LA FUNCIÓN modificar_materia
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return mensaje

import numpy as np
pensum = [
    {
        '0123': {'nombre': 'intro a la ing', 'créditos': 2},
        '4567': {'nombre': 'inglés', 'créditos': 1}
    },
    { 
        
    },
    {

    }
]

m = modificar_materia(pensum, 4, '2345', 'lectoescritura', 3)
print(m)
m = modificar_materia(pensum, 0, '2345', 'lectoescritura', 3)
print(m)
m = modificar_materia(pensum, 2, '2345', 'lectoescritura', 3)
print(m)
m = modificar_materia(pensum, 1, '2345', 'lectoescritura', 3)
print(m)
print(pensum)
m = modificar_materia(pensum, 1, '0123', 'lectoescritura', 3)
print(m)
print(pensum)
