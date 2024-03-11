import pygame
import sys

class Gato:
    def __init__(self):
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
        self.X_IMAGE = pygame.image.load(r'C:\Users\urani\Desktop\Gato\X.png')
        self.O_IMAGE = pygame.image.load(r'C:\Users\urani\Desktop\Gato\O.png')

        # Inicialización del juego
        self.init_game()

    def init_game(self):
        # Variables del juego
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugadores = {'X': 'Jugador 1', 'O': 'Jugador 2'}
        self.opciones_ganadoras = [{(i, j) for i in range(3)} for j in range(3)] + \
                                  [{(i, j) for j in range(3)} for i in range(3)] + \
                                  [{(i, i) for i in range(3)}, {(i, 2-i) for i in range(3)}]
        self.ganador = None
        self.turno = 'X'

    def draw_board(self):
        self.window.fill(self.WHITE)
        pygame.draw.line(self.window, self.BLACK, (100, 0), (100, 300), 5)
        pygame.draw.line(self.window, self.BLACK, (200, 0), (200, 300), 5)
        pygame.draw.line(self.window, self.BLACK, (0, 100), (300, 100), 5)
        pygame.draw.line(self.window, self.BLACK, (0, 200), (300, 200), 5)

    def draw_figure(self, fila, columna):
        if self.tablero[fila][columna] == 'X':
            self.window.blit(self.X_IMAGE, (columna * 100+10, fila * 100+10))
        else:
            self.window.blit(self.O_IMAGE, (columna * 100+10, fila * 100+10))

    def check_winner(self):
        for opcion in self.opciones_ganadoras:
            valores = [self.tablero[i][j] for i, j in opcion]
            if len(set(valores)) == 1 and ' ' not in valores:
                return valores[0]
        if all(all(c != ' ' for c in row) for row in self.tablero):
            return 'Empate'
        return None

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and self.ganador is None:
                    mouse_pos = pygame.mouse.get_pos()
                    if len(mouse_pos) == 2:
                        x, y = mouse_pos
                        fila = y // 100
                        columna = x // 100

                        if self.tablero[fila][columna] == ' ':
                            self.tablero[fila][columna] = self.turno
                            self.ganador = self.check_winner()
                            if self.ganador:
                                if self.ganador == 'Empate':
                                    pygame.display.set_caption("¡Empate!")
                                else:
                                    pygame.display.set_caption(f"¡Ganó {self.jugadores[self.ganador]}!")
                            else:
                                self.turno = 'O' if self.turno == 'X' else 'X'

            self.draw_board()
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] != ' ':
                        self.draw_figure(fila, columna)
            pygame.display.update()

if __name__ == "__main__":
    juego = Gato()
    juego.play()