import pygame
from constants import *

class Renderer:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

    def clear_screen(self):
        self.screen.fill(BOARD_BACKGROUND_COLOR)

    def draw_game_objects(self, snake, apple):
        snake.draw(self.screen)
        apple.draw(self.screen)

    def update_display(self):
        pygame.display.update()