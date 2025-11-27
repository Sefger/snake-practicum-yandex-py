import pygame
from pygame.locals import *
from constants import *

def handle_events(snake):
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        elif event.type == KEYDOWN:
            handle_keydown(event.key, snake)

    return True


def handle_keydown(key, snake):
    if key == K_UP and snake.direction != DOWN:
        snake.next_direction = (0, -1)
    elif key == K_DOWN and snake.direction != (0, -1):
        snake.next_direction = (0, 1)
    elif key == K_LEFT and snake.direction != (1, 0):
        snake.next_direction = (-1, 0)
    elif key == K_RIGHT and snake.direction != (-1, 0):
        snake.next_direction = (1, 0)
    elif key == K_ESCAPE:
        pygame.event.post(pygame.event.Event(QUIT))