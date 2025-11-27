"""
Игровая логика.
"""


def check_apple_collision(snake, apple):
    """
    Проверяет столкновение змейки с яблоком.

    Args:
        snake: Объект змейки
        apple: Объект яблока

    Returns:
        bool: True если было столкновение
    """
    return snake.get_head_position() == apple.position


def reposition_apple(apple, snake):
    """
    Перемещает яблоко на новую позицию.

    Args:
        apple: Объект яблока
        snake: Объект змейки
    """
    apple.randomize_position()
    while apple.position in snake.positions:
        apple.randomize_position()


def update_game_state(snake, apple):
    """
    Обновляет состояние игры.

    Args:
        snake: Объект змейки
        apple: Объект яблока
    """
    snake.update_direction()
    snake.move()

    if check_apple_collision(snake, apple):
        snake.length += 1
        reposition_apple(apple, snake)