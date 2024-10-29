# sudoku_board.py

import pygame
from config import SCREEN, WHITE, GREY, BLACK, RED, FONT, SMALL_FONT, GREEN

class SudokuBoard:
    def __init__(self, tablero, solucion):
        self.tablero = tablero
        self.solucion = solucion
        self.errores = 0
        self.numeros_correctos = set()

    def verificar_numero(self, fila, columna, valor):
        if self.solucion[fila][columna] == valor:
            self.tablero[fila][columna] = valor
            self.numeros_correctos.add((fila, columna))
            return True
        else:
            self.errores += 1
            return False

    def dibujar(self):
        SCREEN.fill(WHITE)
        for i in range(9):
            for j in range(9):
                rect = pygame.Rect(j * 60, i * 60, 60, 60)
                pygame.draw.rect(SCREEN, GREY if self.tablero[i][j] == 0 else WHITE, rect)
                if self.tablero[i][j] != 0:
                    color = GREEN if (i, j) in self.numeros_correctos else (BLACK if self.tablero[i][j] == self.solucion[i][j] else RED)
                    text = FONT.render(str(self.tablero[i][j]), True, color)
                    SCREEN.blit(text, (j * 60 + 20, i * 60 + 10))

        # Dibujar cuadrícula
        for i in range(10):
            width = 4 if i % 3 == 0 else 1
            pygame.draw.line(SCREEN, BLACK, (i * 60, 0), (i * 60, 540), width)
            pygame.draw.line(SCREEN, BLACK, (0, i * 60), (540, i * 60), width)

        # Mostrar errores
        error_text = SMALL_FONT.render(f"Errores: {self.errores}/3", True, RED if self.errores >= 3 else BLACK)
        SCREEN.blit(error_text, (10, 550))
