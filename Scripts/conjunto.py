secuencia = {"manzana", "banano", "pera",8 ,0, False, True}

print(type(secuencia))
print(secuencia)

for s in secuencia:
    print(s)

print(len(secuencia))

secuencia.add("naranja")

print(secuencia)

conjunto = {"mango", "uva", "melocotón"}

#secuencia.update(conjunto)

#print("forma 1",secuencia)

secuenciaconunion = secuencia.union(conjunto)

print("forma 2", secuenciaconunion)

numeros = {0, 9, 2, 3, 4, 5, 6, 7, 8, 1}
letras = {"a", "e", "i", "o", "u"}

numeros.update(letras)
print("el conjunto numeros final es: ",numeros)

secuencia.remove("pera")
print("utilizando remove: ", secuencia)
secuencia.discard("manzana")    #No genera errores
print("utilizando discard: ", secuencia)
secuencia.pop()
print("utilizando pop: ", secuencia)
secuencia.clear()   #limpiar set
print("utilizando clear: ", secuencia)
del secuencia
