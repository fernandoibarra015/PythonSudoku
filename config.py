# config.py

import pygame

# Inicialización de pygame
pygame.init()

# Configuración de pantalla y colores
WIDTH, HEIGHT = 540, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fuentes
FONT = pygame.font.Font(None, 40)
SMALL_FONT = pygame.font.Font(None, 30)
LARGE_FONT = pygame.font.Font(None, 60)

# Configuración del juego
MAX_ERRORES = 3
