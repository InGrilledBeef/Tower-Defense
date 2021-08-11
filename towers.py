# towers.py deals with:
# the towers and their actions
# the movement and speed of the tower's bullets

import pygame
import math
import time
from settings import *
from menu import *
from tilemap import *


class Tower(pygame.sprite.Sprite):
    # this subclass makes a tower
    def __init__(self, game, selected, x, y, colour):
        # add selectX and selectY in param
        self.groups = game.all_sprites, game.towers
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.selected = selected
        self.image.set_alpha(0)
        if self.selected == True:
            self.image.set_alpha(100)


class Bullet(pygame.sprite.Sprite):
    # this subclass deals with the towers' bullets
    def __init__(self, x, y, letter, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE / 2, TILESIZE / 2))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x * TILESIZE, self.y * TILESIZE)
        self.letter = letter
        self.colour = colour
        # there is more than one speed because there is more than 1 target
        self.speedX1 = 0
        self.speedX2 = 0
        self.speedX3 = 0
        self.speedX4 = 0
        self.speedX5 = 0
        self.speedX6 = 0
        self.speedY = 0

        # these if statements deals with the speed of the bullet depending on the tower colour
        if colour == BLUE:
            if (self.letter == 'a' or self.letter == 'b' or self.letter == 'q' or self.letter == 'r'
                    or self.letter == 's' or self.letter == 'H' or self.letter == 'I' or self.letter == 'J'):
                self.speedY = 20

            if (self.letter == 'c' or self.letter == 'd' or self.letter == 'e' or self.letter == 'f'
                    or self.letter == 'g' or self.letter == 'h' or self.letter == 'i'):
                self.speedX1 = -20

            if (self.letter == 'j' or self.letter == 'k' or self.letter == 'l' or self.letter == 'm'
                    or self.letter == 'n' or self.letter == 'o' or self.letter == 'p'):
                self.speedX2 = -20

            if (self.letter == 't' or self.letter == 'u' or self.letter == 'v' or self.letter == 'w'
                    or self.letter == 'x' or self.letter == 'y' or self.letter == 'z'):
                self.speedX3 = -20

            if (self.letter == 'A' or self.letter == 'B' or self.letter == 'C' or self.letter == 'D'
                    or self.letter == 'E' or self.letter == 'F' or self.letter == 'G'):
                self.speedX4 = -20

            if (self.letter == 'K' or self.letter == 'L' or self.letter == 'M' or self.letter == 'N'
                    or self.letter == 'O' or self.letter == 'P' or self.letter == 'Q'):
                self.speedX5 = -20

            if (self.letter == 'R' or self.letter == 'S' or self.letter == 'T' or self.letter == 'U'
                    or self.letter == 'V' or self.letter == 'W' or self.letter == 'X'):
                self.speedX6 = 20

        if colour == VIOLET:
            if (self.letter == 'a' or self.letter == 'b' or self.letter == 'q' or self.letter == 'r'
                    or self.letter == 's' or self.letter == 'H' or self.letter == 'I' or self.letter == 'J'):
                self.speedY = 40

            if (self.letter == 'c' or self.letter == 'd' or self.letter == 'e' or self.letter == 'f'
                    or self.letter == 'g' or self.letter == 'h' or self.letter == 'i'):
                self.speedX1 = -40

            if (self.letter == 'j' or self.letter == 'k' or self.letter == 'l' or self.letter == 'm'
                    or self.letter == 'n' or self.letter == 'o' or self.letter == 'p'):
                self.speedX2 = -40

            if (self.letter == 't' or self.letter == 'u' or self.letter == 'v' or self.letter == 'w'
                    or self.letter == 'x' or self.letter == 'y' or self.letter == 'z'):
                self.speedX3 = -40

            if (self.letter == 'A' or self.letter == 'B' or self.letter == 'C' or self.letter == 'D'
                    or self.letter == 'E' or self.letter == 'F' or self.letter == 'G'):
                self.speedX4 = -40

            if (self.letter == 'K' or self.letter == 'L' or self.letter == 'M' or self.letter == 'N'
                    or self.letter == 'O' or self.letter == 'P' or self.letter == 'Q'):
                self.speedX5 = -40

            if (self.letter == 'R' or self.letter == 'S' or self.letter == 'T' or self.letter == 'U'
                    or self.letter == 'V' or self.letter == 'W' or self.letter == 'X'):
                self.speedX6 = 40

        if colour == INDIGO:
            if (self.letter == 'a' or self.letter == 'b' or self.letter == 'q' or self.letter == 'r'
                    or self.letter == 's' or self.letter == 'H' or self.letter == 'I' or self.letter == 'J'):
                self.speedY = 80

            if (self.letter == 'c' or self.letter == 'd' or self.letter == 'e' or self.letter == 'f'
                    or self.letter == 'g' or self.letter == 'h' or self.letter == 'i'):
                self.speedX1 = -80

            if (self.letter == 'j' or self.letter == 'k' or self.letter == 'l' or self.letter == 'm'
                    or self.letter == 'n' or self.letter == 'o' or self.letter == 'p'):
                self.speedX2 = -80

            if (self.letter == 't' or self.letter == 'u' or self.letter == 'v' or self.letter == 'w'
                    or self.letter == 'x' or self.letter == 'y' or self.letter == 'z'):
                self.speedX3 = -80

            if (self.letter == 'A' or self.letter == 'B' or self.letter == 'C' or self.letter == 'D'
                    or self.letter == 'E' or self.letter == 'F' or self.letter == 'G'):
                self.speedX4 = -80

            if (self.letter == 'K' or self.letter == 'L' or self.letter == 'M' or self.letter == 'N'
                    or self.letter == 'O' or self.letter == 'P' or self.letter == 'Q'):
                self.speedX5 = -80

            if (self.letter == 'R' or self.letter == 'S' or self.letter == 'T' or self.letter == 'U'
                    or self.letter == 'V' or self.letter == 'W' or self.letter == 'X'):
                self.speedX6 = 80

    def update(self):
        # when the bullet reaches a specific point, it returns back to its original spot
        # and it keeps on doing that at a rapid pace to make it look like it is shooting at something
        if self.speedY != 0:
            self.rect.y += self.speedY
            if self.rect.bottom > 11 * TILESIZE:
                self.rect.top = self.y * TILESIZE

        if self.speedX1 != 0:
            self.rect.x += self.speedX1
            if self.rect.left < 5 * TILESIZE:
                self.rect.left = self.x * TILESIZE

        if self.speedX2 != 0:
            self.rect.x += self.speedX2
            if self.rect.left < 15 * TILESIZE:
                self.rect.left = self.x * TILESIZE

        if self.speedX3 != 0:
            self.rect.x += self.speedX3
            if self.rect.left < 24 * TILESIZE:
                self.rect.left = self.x * TILESIZE

        if self.speedX4 != 0:
            self.rect.x += self.speedX4
            if self.rect.left < 33 * TILESIZE:
                self.rect.left = self.x * TILESIZE

        if self.speedX5 != 0:
            self.rect.x += self.speedX5
            if self.rect.left < 42 * TILESIZE:
                self.rect.left = self.x * TILESIZE

        if self.speedX6 != 0:
            self.rect.x += self.speedX6
            if self.rect.right > 57 * TILESIZE:
                self.rect.right = self.x * TILESIZE
