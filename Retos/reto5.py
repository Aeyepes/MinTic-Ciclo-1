#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para el funcionamiento de las librería csv y json respectivamente
import csv, json
import pandas as pd
import numpy as np
"""NOTAS: 
    - PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    - LA CONSOLA TE DIRÁ SI TU SOLUCIÓN ES CORRECTA O NO
    - NO olvidar evaluar tu solución
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)
def validar_accion(data):
    condiciones = [data['Close']>data['Open'],data['Close']<data['Open']]
    opciones = ['SUBE', 'BAJA']

    data['resultado'] = np.select(condiciones, opciones, default = 'ESTABLE')
    return data['resultado']  

def ajuste_cuadratica(data):

    data['resultado'] = ((data['Close'] - data['Adj Close'])**2)**(1/2)
    
    return data['resultado']

def exportar_csv(df_data):
    
    l_date = df_data['Date']
    l_comportamiento = validar_accion(df_data)
    l_cuadratica = ajuste_cuadratica(df_data)

    df_exp_csv = pd.DataFrame(columns = ['Fecha','Comportamiento de la accion','Ajuste Cuadratico de Close'])

    df_exp_csv['Fecha'] = l_date
    df_exp_csv['Comportamiento de la accion'] = l_comportamiento
    df_exp_csv['Ajuste Cuadratico de Close'] = l_cuadratica

    df_exp_csv.to_csv("analisis_archivo.csv", index = False, sep = "\t")

def exportar_json(df):
    dict = {}
    min_open = df['Open'].min()
    max_close = df['Close'].max()
    mean_vol = df['Volume'].mean()

    df['Greatest_difference'] = abs(df['Low'] - df['High'])
    great_diff = df['Greatest_difference'].max()


    for i in df.index:
        if df['Open'][i] == min_open:
            dict['date_lowest_open'] = df['Date'][i]
            dict['lowest_open'] = int(min_open)
        
        if df['Close'][i]  == max_close:
            dict['date_highest_close'] = df['Date'][i]
            dict['highest_close'] = int(max_close)

        if df['Greatest_difference'][i]  == great_diff:
            dict['date_greatest_difference'] = df['Date'][i]
            dict['greatest_difference'] = great_diff
    
    dict['mean_volume'] = mean_vol

    with open('detalles.json','w') as file:
        json.dump(dict,file)



"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    df_data = pd.read_csv('TESLA.csv')
    exportar_csv(df_data)
    exportar_json(df_data)

solucion()