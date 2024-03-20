import pygame
import sys
import tkinter as tk
from tkinter import messagebox
from openai import OpenAI


client = OpenAI(api_key="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")
BalanceIntentos = 1.5

class Gato:
    def __init__(self):
        # Inicialización de Pygame
        pygame.init()

        # Tamaño de la ventana del juego
        self.window_size = (300, 300)

        # Colores
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Configuración de la ventana del juego
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
                                  [{(i, i) for i in range(3)}, {(i, 2 - i) for i in range(3)}]
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
            self.window.blit(self.X_IMAGE, (columna * 100 + 10, fila * 100 + 10))
        else:
            self.window.blit(self.O_IMAGE, (columna * 100 + 10, fila * 100 + 10))

    def Frase_Motivadora(self):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": """
                                                Dame una frase motivacional y coloca ganador:
                                                Motivacional:

                                                Dame una frase de aliento y coloca perdedor:
                                                Alentadora:

                                                Dame una frase de competencia:
                                                Competitiva:
                                                """}
            ],
            max_tokens=500
        )
        return completion.choices[0].message.content

    def check_winner(self):

        for opcion in self.opciones_ganadoras:
            valores = [self.tablero[i][j] for i, j in opcion]
            if len(set(valores)) == 1 and ' ' not in valores:
                ganador = valores[0]
                mensaje = f'¡Felicidades {self.jugadores[ganador]}! ¡Eres el ganador!'
                return ganador, mensaje
        if all(all(c != ' ' for c in row) for row in self.tablero):
            mensaje = '¡Ha sido un empate reñido!'
            return 'Empate', mensaje
        else:
            perdedor = 'X' if self.turno == 'O' else 'O'
            mensaje = f'¡Ánimo {self.jugadores[perdedor]}! ¡Sigue intentándolo!'

            return None, mensaje

    def show_popup(self, message, motivacional):
        root = tk.Tk()
        root.withdraw()
        if message !=  '¡Ha sido un empate reñido!':
            messagebox.showinfo("Resultado", f"{message}\n\n{motivacional}")
        else:
            messagebox.showinfo("Resultado", message)
        root.destroy()

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
                            ganador, mensaje = self.check_winner()
                            if ganador:
                                motivacional = self.Frase_Motivadora()
                                self.show_popup(mensaje, motivacional)
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
