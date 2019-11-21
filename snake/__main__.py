import pygame
import random
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_RIGHT, K_LEFT
from sys import exit

from snake.point import Point
from snake.snake import Snake, Directions


def posicao_aleatoria():
    x = random.randint(0, 630)
    y = random.randint(0, 470)
    return (x // 10 * 10, y // 10 * 10)

def colisao(objetoA, objetoB):
    return (objetoA[0] == objetoB[0]) and (objetoA[1] == objetoB[1])


# Definindo a nossa cobra
snake_pos = Snake(Point(30, 30))

# Definindo a nossa maçã
apple_position = posicao_aleatoria()

direcao = Directions.LEFT # Esquerda


def main():
    global snake_pos, apple_position, direcao

    running = True

    pygame.init()

    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption("Snake em Python com Pygame")

    clock = pygame.time.Clock()

    while running:
        clock.tick(10)

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

        if colisao(snake_pos[0] * 10, apple_position):
            apple_position = posicao_aleatoria()
            snake_pos.eat()

        snake_pos.turn(direcao)
        snake_pos.slither()

        screen.fill((0, 0, 0))
        screen.fill((255, 0, 0), (*apple_position, 10, 10))
        for p in snake_pos:
            screen.fill((0, 255, 0), (p.x * 10, p.y * 10, 10, 10))

        pygame.display.update()

if __name__ == '__main__':
    main()
