# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

from re import A


def tiene_cartas_altas(cartas_siguientes):
    # ACÁ INICIA LA FUNCIÓN

    cartas_altas = 'AJQK'
    
    for cartas in cartas_siguientes:
        if cartas in cartas_altas:
            return True
    return False

    # ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS

def juego(baraja):
    # ACÁ INICIA LA FUNCIÓN
    p1 = 0
    p2 = 0
    switch = 'jugador_1'
    indice = 1
    juego_jugador_1 = []
    juego_jugador_2 = []
    condicion = {'A': 1, 'J': 2, 'Q': 3, 'K':4}
    rango_validar = []
    print('carta','indice', 'puntos', 'switch','puntaje p1', 'puntaje p2', sep="\t")

    for carta in baraja:
        puntos = condicion.get(carta)

        print(carta,indice, puntos, switch, p1, p2, sep="\t\t")

        if puntos == None:
            puntos = 0
        else:
            rango_validar = baraja[indice : indice + puntos]
            if tiene_cartas_altas(rango_validar) or puntos != len(rango_validar):
                puntos = 0
            else:
                puntos = puntos

        if switch == 'jugador_1':
            switch = 'jugador_2'
            p1 += puntos
            juego_jugador_1.append(carta)
        else:
            switch = 'jugador_1'
            p2 += puntos
            juego_jugador_2.append(carta)
        indice += 1

    print('Puntaje\n','jugador_1',p1,'\n\tjugador_2', p2, sep='\t')

    # ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS


baraja = (  '9', '6', '5', '7', 'J', '10', '10', 'K', '8', 'K',
            '9', 'A', '2', 'K', 'K', '4', '10', 'Q', '10', 'Q', 
            '4', '3', '4', '2', 'A', '7', '2', 'J', '3', '6', '5', 
            '5', 'A', '8', '2', 'A', 'J', '8', '8', '6', '3', '3', 
            '9', '5', '6', '7', 'Q', '9', 'Q', '4', 'J', '7') 

juego(baraja)