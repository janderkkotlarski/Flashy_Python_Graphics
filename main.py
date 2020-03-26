import sys
import numpy
import random
import pygame


class Block:

    def __init__(self, window_length, power):
        self.power = power
        self.count = 0
        self.min_perc = 3
        self.med_perc = 10
        self.max_perc = 33.333
        self.base = pow(self.max_perc / self.min_perc, 1 / power)
        self.cur_perc = self.max_perc
        if random.random() < 0.5:
            self.cur_perc = self.min_perc
        else:
            self.base = 1 / self.base
        self.width = window_length * self.cur_perc / 100
        self.height = window_length * self.med_perc * self.med_perc / (100 * self.cur_perc)
        self.pos_x = window_length * random.random()
        self.pos_y = window_length * random.random()
        self.surface = pygame.Surface((int(self.width), int(self.height)))
        self.rect = self.surface.get_rect()
        self.rectposition()
        self.color = 255, 191, 127
        self.surface.fill(self.color)

    def rectposition(self):
        self.rect.centerx = int(self.pos_x)
        self.rect.centery = int(self.pos_y)

    def multiply(self):
        if self.count < self.power:
            self.cur_perc *= self.base
            self.power += 1

    def resize(self):
        self.width = window_length * self.cur_perc / 100
        self.height = window_length * self.med_perc * self.med_perc / (100 * self.cur_perc)

        self.rect.width = int(self.width)

    def blit(self, screen):
        screen.blit(self.surface, self.rect)


pygame.init()

window_length = 768

window_size = window_length, window_length
black = 0, 0, 0

screen = pygame.display.set_mode(window_size)

orange = 255, 127, 0

fps = 100

while 1:

    loops = True

    block = Block(window_length, fps)

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

        block.multiply()
        block.resize()

        block.blit(screen)

        pygame.display.flip()