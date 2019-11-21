import pygame
from pygame.locals import QUIT, KEYDOWN
from sys import exit

from snake.settings import WIDTH, HEIGHT, SCALE, BLACK, RED, GREEN
from snake.geometry import Directions, Point
from snake.characters import Snake, Apple


snake = Snake(Point(30, 30))
apple = Apple(*Point.random())
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
                direcao = Directions.by(event.key)

        if snake.head == apple:
            snake.eat()
            apple = Apple(*Point.random())

        snake.turn(direcao)
        snake.slither()

        screen.fill(BLACK)
        screen.fill(RED, (*(apple * SCALE), SCALE, SCALE))
        for p in snake:
            screen.fill(GREEN, (*(p * SCALE), SCALE, SCALE))

        pygame.display.update()

if __name__ == '__main__':
    main()
