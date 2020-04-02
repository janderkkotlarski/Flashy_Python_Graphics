import sys
import numpy
import random
import pygame


class Block:

    def __init__(self, window_length, tally, color):
        self.tally = tally
        self.count = 0
        self.max_perc = 25
        self.med_perc = 5
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
        self.color = color
        self.past_width = self.width
        self.past_height = self.height
        self.past_color = 127, 95, 63

    def multiply(self, passed):
        reset = False

        if self.count < self.tally:
            self.cur_perc *= pow(self.base, passed / 1000)
            self.count += passed / 1000
        else:
            reset = True
            self.count = 0

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

indigo = 63, 127, 255

green = 127, 255, 127

red = 255, 127, 127

yellow = 255, 255, 127

blue = 127, 127, 255

fps = 500

bpm = 137

beat = 60 / bpm

frames = beat

font = pygame.font.SysFont(None, 50)

while 1:

    loops = True

    block = Block(window_length, frames, blue)

    block_2 = Block(window_length, frames / 2, red)

    block_3 = Block(window_length, frames / 4, yellow)

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
            block.base = 1 / block.base

        if block_2.multiply(passed):
            block_2.base = 1 / block_2.base

        if block_3.multiply(passed):
            block_3.base = 1 / block_3.base

        block.resize()
        block_2.resize()
        block_3.resize()

        block.blit(screen)
        block_2.blit(screen)
        block_3.blit(screen)

        text = font.render(str(passed), True, indigo)
        screen.blit(text, [int(0.2 * window_length), int(0.2 * window_length)])

        text = font.render(str(block.count / block.tally), True, green)
        screen.blit(text, [int(0.8 * window_length), int(0.8 * window_length)])

        pygame.display.flip()