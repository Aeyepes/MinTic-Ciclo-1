def añobisiesto(year):
    if year % 4 == 0:           #paso 1
        if year % 100 == 0:
            if year % 400 == 0:     #paso 2
                return True
            else:
                return False         #paso3
        else:
            return True
    else:
        return False    #paso 5

# year_test = 1612

# array = [1987, 1700, 1900, 2000, 1992, 4000, 2400, 2500, 2016]
años_iterativos = []

# for year in array:
#     print(f'El año {year} es bisiesto? \t{añobisiesto(year)}')

for i in range(1900, 2001):
    if añobisiesto(i) == True:
        años_iterativos.append(int(i))
    
# for year in años_iterativos:
#     print(year)


# for year in años_iterativos:
#     print(f'El año {year} es bisiesto? \t{añobisiesto(year)}')


dct = {'one': 'two', 'three': 'one', 'two' : 'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]
    print(v)

print(v)
