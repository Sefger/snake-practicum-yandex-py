import pygame
import random
from constants import *

class GameObject:
    def __init__(self, position=((SCREEN_WIDTH//2), (SCREEN_HEIGHT//2)), body_color=WHITE):
        self.position = position
        self.body_color = body_color

    def draw (self, surface):
        pass


class Apple(GameObject):
    def __init__(self):
        super().__init__()
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self):
        self.position= (
            random.randint(0, GRID_WIDTH-1)*GRID_SIZE,
            random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        )

    # surface - поверхность для отрисовки
    def draw(self, surface):
        rect = pygame.Rect(
            (self.position[0], self.position[1]),
            (GRID_SIZE, GRID_SIZE)
        )
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(surface, WHITE, rect, 1)


