
tupla = (2022, 7186317, "tipo cadena", "tipo cadena", 2.5, True)
lista = [2022, tupla, 7186317, "tipo cadena", "tipo cadena", 2.5, False]

print("la variable tupla es de tipo: ", type(tupla))
print("la variable lista es de tipo: ", type(lista))

lista[0] = 2021
print(lista)

tuplaconanidacion = (tupla, tupla, tupla)
print(tuplaconanidacion)

print("otra forma de anidar: ")
nuevatupla = (tupla, (1, 2, 3, 4, 5), lista)
print("nuevatupla sin modificar la lista interna: ")
print(nuevatupla)
print("nuevatupla con modificación de la lista interna: ")
lista[0] = "nuevo elemento de la lista"
print(nuevatupla)

