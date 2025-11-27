"""
Обработка пользовательского ввода.
"""
import pygame
from pygame.locals import *
from constants import *


def handle_events(snake):
    """
    Обрабатывает события игры.

    Args:
        snake: Объект змейки для управления

    Returns:
        bool: False если игра должна завершиться
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        elif event.type == KEYDOWN:
            handle_keydown(event.key, snake)

    return True


def handle_keydown(key, snake):
    """
    Обрабатывает нажатия клавиш.

    Args:
        key: Код нажатой клавиши
        snake: Объект змейки для управления
    """
    if key == K_UP and snake.direction != DOWN:
        snake.next_direction = UP
    elif key == K_DOWN and snake.direction != UP:
        snake.next_direction = DOWN
    elif key == K_LEFT and snake.direction != RIGHT:
        snake.next_direction = LEFT
    elif key == K_RIGHT and snake.direction != LEFT:
        snake.next_direction = RIGHT
    elif key == K_ESCAPE:
        pygame.event.post(pygame.event.Event(QUIT))