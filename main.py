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
