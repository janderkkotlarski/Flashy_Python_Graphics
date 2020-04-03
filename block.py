import random
import pygame

class Block:

    def __init__(self, window_length, tally, color, size, scale):
        self.size = size
        self.scale = scale
        self.window_length = window_length
        self.tally = tally
        self.count = 0
        self.max_perc = self.scale * self.size
        self.med_perc = self.size
        self.min_perc = self.size / self.scale
        self.base = pow(self.scale * self.scale, 1 / tally)
        self.cur_perc = self.max_perc
        if random.random() < 0.5:
            self.cur_perc = self.min_perc
        else:
            self.base = 1 / self.base
        self.width = window_length * self.cur_perc / 100
        self.height = window_length * self.med_perc * self.med_perc / (100 * self.cur_perc)
        self.pos_x = window_length * (0.2 + 0.6 * random.random())
        self.pos_y = window_length * (0.2 + 0.6 * random.random())
        self.color = color
        self.past_width = self.width
        self.past_height = self.height
        self.past_color = 127, 95, 63

        self.font = pygame.font.SysFont(None, 50)
        self.indigo = 63, 127, 255
        self.green = 127, 255, 127

    def reset(self):
        self.count = 0

        self.base = pow(self.scale * self.scale, 1 / self.tally)
        self.cur_perc = self.max_perc
        if random.random() < 0.5:
            self.cur_perc = self.min_perc
        else:
            self.base = 1 / self.base

        self.width = self.window_length * self.cur_perc / 100
        self.height = self.window_length * self.med_perc * self.med_perc / (100 * self.cur_perc)
        self.pos_x = self.window_length * (0.2 + 0.6 * random.random())
        self.pos_y = self.window_length * (0.2 + 0.6 * random.random())
        self.past_width = self.width
        self.past_height = self.height

    def multiply(self, passed):
        reset = False

        if self.count < self.tally:
            self.cur_perc *= pow(self.base, passed / 1000)
            self.count += passed / 1000
        else:
            self.reset()

            reset = True

        return reset

    def resize(self):
        self.past_width = self.width
        self.past_height = self.height
        self.width = self.window_length * self.cur_perc / 100
        self.height = self.window_length * self.med_perc * self.med_perc / (100 * self.cur_perc)

        if self.width > self.window_length * self.max_perc / 100:
            self.width = self.window_length * self.max_perc / 100

        if self.height > self.window_length * self.max_perc / 100:
            self.height = self.window_length * self.max_perc / 100

    def blit(self, screen):
        past_surface = pygame.Surface((int(self.past_width), int(self.past_height)))
        past_surface.fill(self.past_color)

        past_rect = past_surface.get_rect()
        past_rect.centerx = int(self.pos_x)
        past_rect.centery = int(self.pos_y)

        screen.blit(past_surface, past_rect)

        text_width = self.font.render(str(self.width), True, self.indigo)
        text_height = self.font.render(str(self.width), True, self.green)

        surface = pygame.Surface((int(self.width), int(self.height)))
        surface.fill(self.color)

        rect = surface.get_rect()
        rect.centerx = int(self.pos_x)
        rect.centery = int(self.pos_y)

        screen.blit(surface, rect)

        # screen.blit(text_width, [int(0.1 * self.window_length), int(0.1 * self.window_length)])
        # screen.blit(text_height, [int(0.1 * self.window_length), int(0.15 * self.window_length)])

