wardrove = {"shirt":["red", "blue", "white"], 
            "jeans":["blue", "black"]}

for llave in wardrove.keys():
    for item in wardrove[llave]:
        print("{item} {llave}".format(item = item, llave = llave))

vestuario = {
    "shirt":["rojo", "azul", "blanco"] ,
    "jean":[]
}

print(vestuario)

for llavevestuario in vestuario.keys():
    for items in vestuario[llavevestuario]:
        print(items, "**", llavevestuario)