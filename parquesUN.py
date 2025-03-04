import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)

# Dimensiones del tablero
ANCHO_CELDA = 35
ALTO_CELDA = 35
DIMENSIONES_TABLERO = 19
ANCHO_VENTANA = ANCHO_CELDA * DIMENSIONES_TABLERO
ALTO_VENTANA = ALTO_CELDA * DIMENSIONES_TABLERO

# Crear ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Tablero de Parqués")

# Definir la matriz del tablero 19x19
tablero = [
    [0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Recorridos de fichas para cada color con coordenadas
RECORRIDOS = {
    "rojo": [(10, 4), (10, 5), (10, 6), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (17, 7), (18, 7), (18, 8), (18, 9), (17, 9), (16, 9), (15, 9), (14, 9), (13, 9), (12, 9), (11, 9), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16), (9, 16), (8, 16), (8, 15), (8, 14), (8, 13), (8, 12), (8, 11), (8, 10), (8, 9), (7, 9), (6, 9), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (0, 9), (0, 8), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)],
    "azul": [(8, 12), (8, 11), (8, 10), (8, 9), (7, 9), (6, 9), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (0, 9), (0, 8), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (9, 0), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (17, 7), (18, 7), (18, 8), (18, 9), (17, 9), (16, 9), (15, 9), (14, 9), (13, 9), (12, 9), (11, 9), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16), (9, 16), (9, 15), (9, 14), (9, 13), (9, 12), (9, 11), (9, 10), (9, 9)],
    "verde": [(14, 9), (13, 9), (12, 9), (11, 9), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16), (9, 16), (8, 16), (8, 15), (8, 14), (8, 13), (8, 12), (8, 11), (8, 10), (8, 9), (7, 9), (6, 9), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (0, 9), (0, 8), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (9, 0), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (17, 7), (18, 7), (18, 8), (17, 8), (16, 8), (15, 8), (14, 8), (13, 8), (12, 8), (11, 8), (10, 8)],
    "amarillo": [(4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (9, 0), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (17, 7), (18, 7), (18, 8), (18, 9), (17, 9), (16, 9), (15, 9), (14, 9), (13, 9), (12, 9), (11, 9), (10, 9), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10), (16, 10), (16, 9), (15, 8), (14, 8), (13, 8), (12, 8), (11, 8), (10, 8), (9, 8), (8, 9), (8, 9), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (9, 0), (8, 0), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)],
}

POSICIONES_SEGURO = [(0, 8), (4, 9), (8, 4), (9, 0), (9, 16), (10, 12), (14, 7), (18, 8)]

# Llegadas
LLEGADAS = {
    "rojo": [(9, 7)],
    "azul": [(9, 9)],
    "amarillo": [(8, 8)],
    "verde": [(10, 8)]
}

# Posiciones iniciales de fichas
posiciones_fichas = {
    "rojo": [(13, 4), (12, 4), (13, 5), (12, 5)],
    "azul": [(5, 11), (6, 12), (5, 12), (6, 11)],
    "verde": [(13, 11), (13, 12), (12, 12), (12, 11)],
    "amarillo": [(5, 4), (5, 5), (6, 4), (6, 5)],
}

turno_actual = "rojo"  # Turno inicial

# Función para dibujar el tablero
def dibujar_tablero():
    ventana.fill(BLANCO)
    for fila in range(DIMENSIONES_TABLERO):
        for columna in range(DIMENSIONES_TABLERO):
            color = BLANCO
            if tablero[fila][columna] == 1:
                color = ROJO
            elif tablero[fila][columna] == 2:
                color = AZUL
            elif tablero[fila][columna] == 3:
                color = VERDE
            elif tablero[fila][columna] == 4:
                color = AMARILLO
            pygame.draw.rect(ventana, color, (columna * ANCHO_CELDA, fila * ALTO_CELDA, ANCHO_CELDA, ALTO_CELDA))
            pygame.draw.rect(ventana, NEGRO, (columna * ANCHO_CELDA, fila * ALTO_CELDA, ANCHO_CELDA, ALTO_CELDA), 1)

    # Dibujar fichas con contorno negro y nombre
    for color in posiciones_fichas:
        for i, ficha in enumerate(posiciones_fichas[color]):
            fila, columna = ficha
            nombre_ficha = f"{color[0]}{i+1}"  # Formatear el nombre (R1, A2, etc.)
            if color == "rojo":
                pygame.draw.circle(ventana, ROJO, (columna * ANCHO_CELDA + ANCHO_CELDA // 4, fila * ALTO_CELDA + ALTO_CELDA // 4), 10)
            elif color == "azul":
                pygame.draw.circle(ventana, AZUL, (columna * ANCHO_CELDA + ANCHO_CELDA // 4, fila * ALTO_CELDA + ALTO_CELDA // 4), 10)
            elif color == "verde":
                pygame.draw.circle(ventana, VERDE, (columna * ANCHO_CELDA + ANCHO_CELDA // 4, fila * ALTO_CELDA + ALTO_CELDA // 4), 10)
            elif color == "amarillo":
                pygame.draw.circle(ventana, AMARILLO, (columna * ANCHO_CELDA + ANCHO_CELDA // 4, fila * ALTO_CELDA + ALTO_CELDA // 4), 10)

            # Dibujar el contorno negro
            pygame.draw.circle(ventana, NEGRO, (columna * ANCHO_CELDA + ANCHO_CELDA // 4, fila * ALTO_CELDA + ALTO_CELDA // 4), 10, 1)

            # Dibujar el nombre de la ficha (ajustar la fuente y tamaño según sea necesario)
            font = pygame.font.Font(None, 15)  # Fuente y tamaño de la letra
            text = font.render(nombre_ficha, True, NEGRO)
            text_rect = text.get_rect(center=(columna * ANCHO_CELDA + ANCHO_CELDA // 4, fila * ALTO_CELDA + ALTO_CELDA // 4))
            ventana.blit(text, text_rect)

    # Dibujar las posiciones de seguro
    for pos in POSICIONES_SEGURO:
        pygame.draw.circle(ventana, NEGRO, (pos[1] * ANCHO_CELDA + ANCHO_CELDA // 2,
                                            pos[0] * ALTO_CELDA + ALTO_CELDA // 2), ANCHO_CELDA // 4)

    # Dibujar llegadas
    for color, posiciones in LLEGADAS.items():
        for pos in posiciones:
            pygame.draw.circle(ventana, NEGRO, (pos[1] * ANCHO_CELDA + ANCHO_CELDA // 2,
                                                pos[0] * ALTO_CELDA + ALTO_CELDA // 2), ANCHO_CELDA // 2, 3)

    pygame.display.flip()

def lanzar_dados():
    """Función para lanzar dos dados."""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def mover_ficha(color, num_ficha, pasos):
    """Mueve la ficha del color dado, identificada por su número, una cantidad de pasos."""
    ficha_pos = posiciones_fichas[color][num_ficha]  # Obtener la posición actual de la ficha
    recorrido = RECORRIDOS[color]  # Obtener el recorrido del color

    if ficha_pos in recorrido:  # Si la ficha está en el recorrido
        indice = recorrido.index(ficha_pos)  # Obtener la posición en el recorrido
        nueva_posicion = indice + pasos  # Calcular la nueva posición

        if nueva_posicion < len(recorrido):
            posiciones_fichas[color][num_ficha] = recorrido[nueva_posicion]  # Mover ficha
        else:
            posiciones_fichas[color][num_ficha] = LLEGADAS[color][0]  # Ficha llega a la meta
    else:
        # Si la ficha está en la posición de salida, la movemos al inicio del recorrido
        posiciones_fichas[color][num_ficha] = recorrido[0]

    # Verificar si se captura otra ficha
    capturar_ficha(posiciones_fichas[color][num_ficha])

def capturar_ficha(posicion):
    """Verifica si hay una ficha de otro color en la misma posición y la captura."""
    for color in posiciones_fichas:
        for i in range(len(posiciones_fichas[color])):
            if posiciones_fichas[color][i] == posicion:
                posiciones_fichas[color][i] = posiciones_fichas[color][i]  # Volver a la posición inicial

def manejar_eventos():
    """Maneja los eventos del juego, como el clic del mouse para lanzar el dado y mover fichas."""
    global turno_actual
    intentos_sin_cinco = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:  # Si se hace clic
            dado1, dado2 = lanzar_dados()  # Lanzar dos dados
            print(f"{turno_actual} ha sacado un {dado1} y un {dado2}.")

            puede_mover = (dado1 == 5) or (dado2 == 5) or (dado1 + dado2 == 5)

            if puede_mover:
                intentos_sin_cinco = 0  # Reiniciar contador de intentos

                # Mover las fichas según los dados (simplificado para este ejemplo)
                # Aquí puedes implementar una lógica más compleja para elegir qué fichas mover y en qué orden
                mover_ficha(turno_actual, 0, dado1) 
                mover_ficha(turno_actual, 1, dado2)

                # Cambiar el turno al siguiente jugador
                turno_actual = siguiente_turno(turno_actual)
            else:
                intentos_sin_cinco += 1
                if intentos_sin_cinco >= 3:
                    print("Has agotado tus intentos. Se pasa el turno.")
                    intentos_sin_cinco = 0
                    turno_actual = siguiente_turno(turno_actual)
                

def siguiente_turno(turno_actual):
    """Devuelve el color del siguiente jugador, siguiendo el orden establecido."""
    colores = ["rojo", "verde", "azul", "amarillo"]
    indice_actual = colores.index(turno_actual)
    siguiente_indice = (indice_actual + 1) % len(colores)
    return colores[siguiente_indice]

# Bucle principal del juego
def bucle_juego():
    while True:
        manejar_eventos()  # Manejar eventos
        dibujar_tablero()  # Dibujar el tablero
        pygame.time.wait(300)  # Pequeña pausa para controlar la velocidad del bucle

bucle_juego()
