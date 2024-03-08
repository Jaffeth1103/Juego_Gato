import pygame
import sys

class Gato:
    def _init_(self):
        # Inicialización de Pygame
        pygame.init()

        # Tamaño de la ventana
        self.window_size = (300, 300)

        # Colores
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Configuración de la ventana
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Gato")

        # Cargar imágenes
        self.X_IMAGE = pygame.image.load(r'C:\Users\urani\Desktop\Programa Gato\X.png')
        self.O_IMAGE = pygame.image.load(r'C:\Users\urani\Desktop\Programa Gato\O.png')

        # 1. Comprensión de listas con condicionales
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        # 2. Comprensión de diccionarios
        self.jugadores = {'X': 'Jugador 1', 'O': 'Jugador 2'}
        # 3. Comprensión conjuntos
        self.opciones_ganadoras = [{(i, j) for i in range(3)} for j in range(3)] + \
                                  [{(i, j) for j in range(3)} for i in range(3)] + \
                                  [{(i, i) for i in range(3)}, {(i, 2-i) for i in range(3)}]
        # 4. Empaquetamiento de variables/ZIP variables
        self.ganador = None
        self.turno = 'X'
