# game_manager.py

import pygame
from config import SCREEN, WIDTH, HEIGHT, WHITE, RED, GREY, LARGE_FONT, SMALL_FONT, BLACK

class GameManager:
    def __init__(self, board):
        self.board = board

    def mostrar_game_over(self):
        SCREEN.fill(WHITE)
        
        # Mensaje de Game Over
        game_over_text = LARGE_FONT.render("¡Game Over!", True, RED)
        SCREEN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3 - game_over_text.get_height() // 2))
        
        # Botón "Reintentar"
        retry_text = SMALL_FONT.render("Reintentar", True, WHITE)
        self.retry_rect = pygame.Rect(WIDTH // 4 - 60, HEIGHT // 2, 120, 50)
        pygame.draw.rect(SCREEN, GREY, self.retry_rect, border_radius=10)
        pygame.draw.rect(SCREEN, BLACK, self.retry_rect, width=2, border_radius=10)  # Borde negro
        SCREEN.blit(retry_text, (self.retry_rect.x + (self.retry_rect.width - retry_text.get_width()) // 2, self.retry_rect.y + 10))
        
        # Botón "Salir"
        exit_text = SMALL_FONT.render("Salir", True, WHITE)
        self.exit_rect = pygame.Rect(3 * WIDTH // 4 - 60, HEIGHT // 2, 120, 50)
        pygame.draw.rect(SCREEN, GREY, self.exit_rect, border_radius=10)
        pygame.draw.rect(SCREEN, BLACK, self.exit_rect, width=2, border_radius=10)  # Borde negro
        SCREEN.blit(exit_text, (self.exit_rect.x + (self.exit_rect.width - exit_text.get_width()) // 2, self.exit_rect.y + 10))
        
        pygame.display.flip()

    def manejar_click(self, pos):
        """Maneja los clics en los botones 'Reintentar' y 'Salir'."""
        if self.retry_rect.collidepoint(pos):
            return "reintentar"
        elif self.exit_rect.collidepoint(pos):
            return "salir"
        return None
