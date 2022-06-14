from lib2to3.pytree import type_repr
from typing import final


particiones = 1

for i in range(10):
    try:
        particiones /= i
    except:
        print('división por cero, el ciclo ignorará la operación')
    finally:
        print('división parcial:', particiones)

print(particiones)

a = 'a'
try:
    print(a/5)
except TypeError as e:
    print('error de tipo de datos')
    raise TypeError('error de tipos de datos')
    # print('error: ', e, sep='\n')
except ZeroDivisionError as e:
    print('division por cero')
    print(e)