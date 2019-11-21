from random import randrange

import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_RIGHT, K_LEFT
from sys import exit

from snake.settings import WIDTH, HEIGHT, SCALE, BLACK, RED, GREEN
from snake.characters import Snake, Directions, Point, Apple


def random_point():
    return Point(randrange(63), randrange(47))


snake = Snake(Point(30, 30))
apple = Apple(*random_point())
direcao = Directions.LEFT


def main():
    global snake, apple, direcao

    running = True

    pygame.init()

    screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE), 0, 32)
    pygame.display.set_caption("Stallone Cobra")

    clock = pygame.time.Clock()

    while running:
        clock.tick(10)  #TODO: Usar um Tick que não bloquei a execução.

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    direcao = Directions.UP
                if event.key == K_DOWN:
                    direcao = Directions.DOWN
                if event.key == K_RIGHT:
                    direcao = Directions.RIGHT
                if event.key == K_LEFT:
                    direcao = Directions.LEFT

        if snake[0] == apple:
            apple = Apple(*random_point())
            snake.eat()

        snake.turn(direcao)
        snake.slither()

        screen.fill(BLACK)
        screen.fill(RED, (*(apple * SCALE), SCALE, SCALE))
        for p in snake:
            screen.fill(GREEN, (*(p * SCALE), SCALE, SCALE))

        pygame.display.update()

if __name__ == '__main__':
    main()
