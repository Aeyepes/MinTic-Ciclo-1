#declarando un diccionario
diccionario = {"unaclavequeNOexiste":10,"cadena2":[1,2,3,4],"cadena3":10,"cadena4":"valor"}

print(diccionario)

#llamando un solo elemento
print(diccionario["cadena2"])

#preguntar por una clave
print("clave" in diccionario)
print("unaclavequeNOexiste" in diccionario)
print("realizo una operación sobre un valor:")
a = diccionario["unaclavequeNOexiste"]
print(a*10)         #Son lo mismo que: print(diccionario[unaclavequeNOexiste]*10)

diccionario2 = {"1": ["Rafael", "Medellín"],
                "2": ["Juan", "password"],
                "3": [10, "Ana"],
                "Pablo":10}

print("1" in diccionario2)