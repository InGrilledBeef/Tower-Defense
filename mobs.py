# mobs.py contains the Mob subclass
# deals with creating the mobs and their movements

import pygame
import os
import random
from settings import *


class Mob(pygame.sprite.Sprite):
    # this subclass makes mobs
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 9
        self.health = 1
        # the mobs are given a random choice of these speeds
        speeds = [0.0625, 0.25, 0.5, 1]
        value = random.randint(0, 3)
        speed = speeds[value]
        self.speedx = speed
        self.speedy = speed

    def move(self):
        # Algorithm for mob movement based on map
        if self.rect.top == 9 * TILESIZE and (
                (0 <= self.rect.left < 7 * TILESIZE) or (16 * TILESIZE <= self.rect.left < 25 * TILESIZE) or (
                34 * TILESIZE <= self.rect.left < 43 * TILESIZE)):
            self.x += self.speedx
        if self.rect.top == 36 * TILESIZE and ((7 * TILESIZE <= self.rect.left < 16 * TILESIZE) or (
                25 * TILESIZE <= self.rect.left < 34 * TILESIZE) or (43 * TILESIZE <= self.rect.left < 55 * TILESIZE)):
            self.x += self.speedx
        if self.rect.top < 36 * TILESIZE and (
                self.rect.left == 7 * TILESIZE or self.rect.left == 25 * TILESIZE or self.rect.left == 43 * TILESIZE):
            self.y += self.speedy
        if self.rect.top > 9 * TILESIZE and (
                self.rect.left == 16 * TILESIZE or self.rect.left == 34 * TILESIZE or self.rect.left == 55 * TILESIZE):
            self.y -= self.speedy
        if self.rect.left == 55 * TILESIZE:
            self.y -= self.speedy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

        # here is where the move function is called
        self.move()

