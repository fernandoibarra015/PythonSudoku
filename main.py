# main.py

import pygame
from config import SCREEN, WIDTH, HEIGHT, MAX_ERRORES
from sudoku_generator import crear_tablero_juego
from sudoku_board import SudokuBoard
from game_manager import GameManager

def iniciar_juego():
    """Función que inicializa el tablero de juego y el estado del juego."""
    tablero_juego, solucion = crear_tablero_juego("Fácil")
    board = SudokuBoard(tablero_juego, solucion)
    return board, GameManager(board)

def main():
    pygame.init()
    board, game_manager = iniciar_juego()
    selected = None
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_over:
                    accion = game_manager.manejar_click(event.pos)
                    if accion == "reintentar":
                        board, game_manager = iniciar_juego()  # Reinicia el juego
                        game_over = False
                    elif accion == "salir":
                        running = False
                else:
                    x, y = pygame.mouse.get_pos()
                    if y < 540:
                        selected = (y // 60, x // 60)
            elif event.type == pygame.KEYDOWN and selected and not game_over:
                fila, columna = selected
                if board.tablero[fila][columna] == 0:
                    valor = event.key - pygame.K_0  # Convierte el número presionado
                    if 1 <= valor <= 9:
                        board.verificar_numero(fila, columna, valor)
                selected = None

        if not game_over:
            board.dibujar()
            pygame.display.flip()

        if board.errores >= MAX_ERRORES and not game_over:
            game_manager.mostrar_game_over()
            game_over = True

    pygame.quit()

if __name__ == "__main__":
    main()
