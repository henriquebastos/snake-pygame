import pygame
from pygame.locals import QUIT, KEYDOWN
from sys import exit

from snake.settings import WIDTH, HEIGHT, SCALE, VELOCITY, GAME_CAPTION, Colour
from snake.geometry import Directions, Point
from snake.characters import Snake, Apple


snake = Snake(Point(30, 30))
apple = Apple(*Point.random())
direction = Directions.LEFT


def main():
    global snake, apple, direction

    running = True

    pygame.init()
    screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE), 0, 32)
    pygame.display.set_caption(GAME_CAPTION)
    clock = pygame.time.Clock()

    while running:
        clock.tick(VELOCITY)  #TODO: Usar um Tick que não bloqueie a execução.

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN:
                direction = Directions.by(event.key, direction)

        if snake.head == apple:
            snake.eat()
            apple = Apple(*Point.random())

        snake.turn(direction)
        snake.slither()

        screen.fill(Colour.BLACK)
        screen.fill(Colour.RED, (*(apple * SCALE), SCALE, SCALE))
        for p in snake:
            screen.fill(snake.colour, (*(p * SCALE), SCALE, SCALE))

        pygame.display.update()


if __name__ == '__main__':
    main()
