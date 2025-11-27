import pygame
import random
from constants import *

class GameObject:
    def __init__(self, positions=((SCREEN_WIDTH//2), (SCREEN_HEIGHT//2)), body_color=WHITE):
        self.positions = positions
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

class Snake(GameObject):
    def __init__(self):
        super().__init__()
        self.body_color = SNAKE_COLOR
        self.reset()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH//2), (SCREEN_HEIGHT//2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.next_direction = None
        self.last = None


    def update_direction(self):
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        head = self.get_head_position()
        x, y = self.direction
        new_x = (head[0]+(x*GRID_SIZE)%SCREEN_WIDTH)
        new_y = (head[1] + (y * GRID_SIZE))%SCREEN_HEIGHT
        new_position = (new_x, new_y)

        if new_position in self.positions[1:]:
            self.reset()
            return

        if len(self.positions)>=self.length:
            self.last = self.positions[-1]

        self.positions.insert(0, new_position)

        if len(self.positions)>self.length:
            self.positions.pop()

        def draw(self, surface):
            if self.last:
                last_rect = pygame.Rect(
                    (self.last[0], self.last[1]),
                    (GRID_SIZE, GRID_SIZE)
                )
                pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, last_rect)

            for position in self.positions:
                rect = pygame.Rect(
                    (position[0], position[1]),
                    (GRID_SIZE, GRID_SIZE)
                )
                pygame.draw.rect(surface, self.body_color, rect)
                pygame.draw.rect(surface, WHITE, rect, 1)