
import random

# Crear el tablero
def crear_tablero(tamaño):
    return [['~' for _ in range(tamaño)] for _ in range(tamaño)]

# Imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))

# Colocar barcos en el tablero
def colocar_barcos(tablero, tamaño_barco):
    tamaño = len(tablero)
    for _ in range(tamaño_barco):
        barco_colocado = False
        while not barco_colocado:
            orientacion = random.choice(['H', 'V'])
            fila = random.randint(0, tamaño - 1)
            columna = random.randint(0, tamaño - 1)
            if orientacion == 'H' and columna + tamaño_barco <= tamaño:
                if all(tablero[fila][columna + i] == '~' for i in range(tamaño_barco)):
                    for i in range(tamaño_barco):
                        tablero[fila][columna + i] = 'B'
                    barco_colocado = True
            elif orientacion == 'V' and fila + tamaño_barco <= tamaño:
                if all(tablero[fila + i][columna] == '~' for i in range(tamaño_barco)):
                    for i in range(tamaño_barco):
                        tablero[fila + i][columna] = 'B'
                    barco_colocado = True

# Atacar una posición en el tablero
def atacar(tablero, fila, columna):
    if tablero[fila][columna] == 'B':
        tablero[fila][columna] = 'X'
        return True
    elif tablero[fila][columna] == '~':
        tablero[fila][columna] = 'O'
        return False

# Juego principal
def juego():
    tamaño = 10
    tamaño_barco = 5
    tablero_jugador = crear_tablero(tamaño)
    tablero_computadora = crear_tablero(tamaño)
    colocar_barcos(tablero_computadora, tamaño_barco)
    
    print("¡Bienvenido a Hundir la Flota!")
    imprimir_tablero(tablero_jugador)
    
    while True:
        try:
            fila = int(input("Introduce la fila (0-9): "))
            columna = int(input("Introduce la columna (0-9): "))
        except ValueError:
            # Este bloque se ejecuta si hay un error de tipo ValueError
            print("¡Eso no es un número válido!")
        if atacar(tablero_computadora, fila, columna):
            print("¡Tocado!")
        else:
            print("¡Agua!")
        imprimir_tablero(tablero_computadora)
        
        if all(celda != 'B' for fila in tablero_computadora for celda in fila):
            print("¡Has hundido todos los barcos!")
            break

juego()