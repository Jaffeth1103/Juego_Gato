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

# Dibujar el tablero
    def dibujar_tablero(self):
        self.window.fill(self.WHITE)
        pygame.draw.line(self.window, self.BLACK, (100, 0), (100, 300), 5)
        pygame.draw.line(self.window, self.BLACK, (200, 0), (200, 300), 5)
        pygame.draw.line(self.window, self.BLACK, (0, 100), (300, 100), 5)
        pygame.draw.line(self.window, self.BLACK, (0, 200), (300, 200), 5)
            
 # Dibujar X o O en el tablero
    def dibujar_figura(self, fila, columna):
        if self.tablero[fila][columna] == 'X':
            self.window.blit(self.X_IMAGE, (columna * 100+10, fila * 100+10))
        else:
            self.window.blit(self.O_IMAGE, (columna * 100+10, fila * 100+10))
                    
  # 6. Desempaquetamiento en argumentos de funciones
    def verificar_ganador(self):
        for opcion in self.opciones_ganadoras:
            valores = [self.tablero[i][j] for i, j in opcion]
            if len(set(valores)) == 1 and ' ' not in valores:
                return valores[0]
        return None
    
 # 7. Desempaquetamiento extendido
    def jugar(self):
        while self.ganador is None:
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
                            self.ganador = self.verificar_ganador()
                            if self.ganador:
                                print(f"¡Felicidades {self.jugadores[self.ganador]}! ¡Has ganado!")
                            elif all(all(c != ' ' for c in row) for row in self.tablero):
                                print("¡Empate!")
                                break
                            # Cambiar el turno del jugador
                            self.turno = 'O' if self.turno == 'X' else 'X'

            self.dibujar_tablero()
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] != ' ':
                        self.dibujar_figura(fila, columna)
            pygame.display.update()

if __name__ == "__main__":
    juego = Gato()
    juego.jugar()    
