import sys
import numpy
import random
import pygame

from block import Block

pygame.init()

window_length = 768

window_size = window_length, window_length
black = 0, 0, 0

screen = pygame.display.set_mode(window_size)

orange = 255, 127, 0

indigo = 63, 127, 255

green = 127, 255, 127

red = 255, 127, 127

yellow = 255, 255, 127

blue = 127, 127, 255

fps = 250

bpm = 120

beat = 60 / bpm

frames = beat

size = 5

scale = 100

font = pygame.font.SysFont(None, 50)

while 1:

    loops = True

    block_0 = Block(window_length, 2 * frames, blue, 1.4 * size, scale)

    block_1 = Block(window_length, frames, green, size , scale / 2)

    block_2 = Block(window_length, frames / 1.4, yellow, size / 2, scale / 4)

    block_3 = Block(window_length, frames / 4, red, size / 2, scale / 8)

    clock = pygame.time.Clock()

    while loops:
        passed = clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_RETURN:
                    loops = False

        screen.fill(black)

        # screen.blit(surface, rect)

        block_0.multiply(passed)
        block_1.multiply(passed)
        block_2.multiply(passed)
        block_3.multiply(passed)

        block_0.resize()
        block_1.resize()
        block_2.resize()
        block_3.resize()

        block_0.blit(screen)
        block_1.blit(screen)
        block_2.blit(screen)
        block_3.blit(screen)

        # text = font.render(str(passed), True, indigo)
        # screen.blit(text, [int(0.2 * window_length), int(0.2 * window_length)])

        # text = font.render(str(int(1000 * block.count)), True, green)
        # screen.blit(text, [int(0.8 * window_length), int(0.8 * window_length)])

        pygame.display.flip()