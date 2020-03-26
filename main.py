import sys
import numpy
import random
import pygame


class Block:

    def __init__(self, window_length, tally):
        self.tally = tally
        self.count = 0
        self.max_perc = 50
        self.med_perc = 10
        self.min_perc = self.med_perc * self.med_perc / self.max_perc
        self.base = pow(self.max_perc / self.min_perc, 1 / tally)
        self.cur_perc = self.max_perc
        if random.random() < 0.5:
            self.cur_perc = self.min_perc
        else:
            self.base = 1 / self.base
        self.width = window_length * self.cur_perc / 100
        self.height = window_length * self.med_perc * self.med_perc / (100 * self.cur_perc)
        self.pos_x = window_length * random.random()
        self.pos_y = window_length * random.random()
        self.color = 255, 191, 127
        self.past_width = self.width
        self.past_height = self.height
        self.past_color = 127, 95, 63

    def multiply(self, passed):
        reset = False

        if self.count < self.tally:
            self.cur_perc *= pow(self.base, passed * self.tally / 1000)
            self.count += passed * self.tally / 1000
        else:
            reset = True

        return reset


    def resize(self):
        self.past_width = self.width
        self.past_height = self.height
        self.width = window_length * self.cur_perc / 100
        self.height = window_length * self.med_perc * self.med_perc / (100 * self.cur_perc)

    def blit(self, screen):
        past_surface = pygame.Surface((int(self.past_width), int(self.past_height)))
        past_surface.fill(self.past_color)

        past_rect = past_surface.get_rect()
        past_rect.centerx = int(self.pos_x)
        past_rect.centery = int(self.pos_y)

        screen.blit(past_surface, past_rect)

        surface = pygame.Surface((int(self.width), int(self.height)))
        surface.fill(self.color)

        rect = surface.get_rect()
        rect.centerx = int(self.pos_x)
        rect.centery = int(self.pos_y)

        screen.blit(surface, rect)


pygame.init()

window_length = 768

window_size = window_length, window_length
black = 0, 0, 0

screen = pygame.display.set_mode(window_size)

orange = 255, 127, 0

fps = 100

while 1:

    loops = True

    block = Block(window_length, fps / 16)

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

        if block.multiply(passed):
            loops = False

        block.resize()

        block.blit(screen)

        pygame.display.flip()