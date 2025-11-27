import pygame
from constants import FPS
from game_objects import Snake, Apple
from input_handler import handle_events
from game_logic import update_game_state
from renderer import Renderer

def main():
    pygame.init()
    clock = pygame.time.Clock()

    renderer = Renderer()

    snake = Snake()
    apple = Apple()

    running = True
    while running:
        running = handle_events(snake)
        update_game_state(snake, apple)

        renderer.clear_screen()
        renderer.draw_game_objects(snake,apple)
        renderer.update_display()

        clock.tick(FPS)
    pygame.quit()

if __name__=='__main__':
    main()