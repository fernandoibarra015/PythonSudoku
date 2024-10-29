# sudoku_generator.py

import numpy as np
import random

def es_valido(tablero, fila, columna, valor):
    for i in range(9):
        if tablero[fila][i] == valor or tablero[i][columna] == valor:
            return False
    inicio_fila = (fila // 3) * 3
    inicio_columna = (columna // 3) * 3
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == valor:
                return False
    return True

def generar_sudoku():
    base = 3
    lado = base * base
    nums = np.random.permutation(range(1, lado + 1))
    board = np.zeros((lado, lado), dtype=int)

    def backtrack():
        for i in range(lado):
            for j in range(lado):
                if board[i][j] == 0:
                    random.shuffle(nums)
                    for num in nums:
                        if es_valido(board, i, j, num):
                            board[i][j] = num
                            if backtrack():
                                return True
                            board[i][j] = 0
                    return False
        return True

    backtrack()
    return board

def crear_tablero_juego(dificultad="Fácil"):
    sudoku_completo = generar_sudoku()
    tablero_juego = sudoku_completo.copy()
    vacios = 20 if dificultad == "Fácil" else 35 if dificultad == "Medio" else 50
    for _ in range(vacios):
        x, y = random.randint(0, 8), random.randint(0, 8)
        tablero_juego[x][y] = 0
    return tablero_juego, sudoku_completo
