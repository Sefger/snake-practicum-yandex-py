"""
Отрисовка игровых объектов.
"""
import pygame
from constants import *


class Renderer:
    """Класс для управления отрисовкой."""

    def __init__(self):
        """Инициализирует рендерер."""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

    def clear_screen(self):
        """Очищает экран."""
        self.screen.fill(BOARD_BACKGROUND_COLOR)

    def draw_game_objects(self, snake, apple):
        """
        Отрисовывает игровые объекты.

        Args:
            snake: Объект змейки
            apple: Объект яблока
        """
        snake.draw(self.screen)
        apple.draw(self.screen)

    def update_display(self):
        """Обновляет отображение."""
        pygame.display.update()