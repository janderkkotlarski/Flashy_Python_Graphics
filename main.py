import sys
import numpy
import pygame


class Block:

    def __init__(self):
        self.surface = pygame.Surface((64, 64))
        self.color = 255, 191, 127
        self.surface.fill(self.color)

    def blit(self, screen):
        screen.blit(self.surface, self.surface.get_rect())


pygame.init()

window_length = 768

window_size = window_length, window_length
black = 0, 0, 0

screen = pygame.display.set_mode(window_size)

orange = 255, 127, 0

surface = pygame.Surface((128, 128))

rect = surface.get_rect()

surface.fill(orange)

block = Block()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    screen.fill(black)

    screen.blit(surface, rect)

    block.blit(screen)

    pygame.display.flip()