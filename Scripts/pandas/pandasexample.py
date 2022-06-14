from numpy import NAN
import pandas as pd

df = pd.read_csv("./atleta.csv", sep = ";")
#df = pd.read_csv("https://raw.githubusercontent.com/DiegOliveros/Programacion-C1-Python/main/C%C3%B3digo%20Clase/S4%202022%2005%2010/atleta2.csv", sep = ",")

#print(df.to_string())#todo el archivo
print(df.columns)
print(df.head(5))
# print(df.tail(5))
# print(df.describe())

df2 = df.loc[0:2]
print(type(df.loc[2]))
# print(df["     Duration "]==60)

#Recorrer los valores de una fila
# for i in df2.loc[0]:
#     print(i)

#Cuantas personas tienen el pulso entre 100 y 120
count = 0
serie = (df.loc[::])[' Pulse  ']
serie2 = df.filter([' Pulse  '])

serie3 = df.iloc[:,2]


def sano(serie, rango):
    count = 0
    for i in serie:
        if rango[0] <= i <= rango[1]:
            count += 1
    return count
rango =[136, 150]
print(f"Los atletas que tienen el pulso entre {rango[0]} y {rango[1]} son: {sano(serie, rango)}")
