import sys
import numpy
import random
import pygame


def random_length(min_perc, max_perc):
    return min_perc + (max_perc - min_perc)*random.random()


class Block:

    def __init__(self, window_length):
        self.min_perc = 3
        self.med_perc = 10
        self.max_perc = 33.333
        self.cur_perc = random_length(self.min_perc, self.max_perc)
        self.width = window_length * self.cur_perc / 100
        self.height = window_length * self.med_perc * self.med_perc / (100 * self.cur_perc)
        self.surface = pygame.Surface((int(self.width), int(self.height)))
        self.color = 255, 191, 127
        self.surface.fill(self.color)

    def resize(self):
        self.width = window_length * self.cur_perc / 100
        self.height = window_length * self.med_perc * self.med_perc / (100 * self.cur_perc)

    def blit(self, screen):
        screen.blit(self.surface, self.surface.get_rect())


pygame.init()

window_length = 768

window_size = window_length, window_length
black = 0, 0, 0

screen = pygame.display.set_mode(window_size)

orange = 255, 127, 0

while 1:

    loops = True

    block = Block(window_length)

    while loops:
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

        block.blit(screen)

        pygame.display.flip()