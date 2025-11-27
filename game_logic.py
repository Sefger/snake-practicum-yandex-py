from constants import *

def check_apple_collision(snake, apple):
    if snake.get_head_position() == apple.position:
        snake.length +=1
        return True
    return False

def reposition_apple(snake, apple):
    apple.randomize_position()
    while apple.position in snake.positions:
        apple.randomize_position()

def update_game_state(snake, apple):
    snake.update_direction()
    snake.move()

    if check_apple_collision(snake, apple):
        reposition_apple(snake, apple)