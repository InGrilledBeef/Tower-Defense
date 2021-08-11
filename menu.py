# menu.py deals with the buttons appears on the menu
# includes subclasses for each button

import pygame
import os
from settings import *
pygame.font.init()

class BlueButton(pygame.sprite.Sprite):
    # This sets the position of the blue button. This is similar to VioletButton and Indigo Button
    # except they have their own positions and colours
    def __init__(self, game, selected):
        self.groups = game.all_sprites, game.button
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((2 * TILESIZE, 2 * TILESIZE))
        self.rect = self.image.get_rect()
        self.selected = selected
        self.x = 65
        self.y = 14
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

        # when selected, the colour is changed to show that it is selected
        if self.selected == True:
            self.image.fill(GREENBLUE)
        else:
            self.image.fill(BLUE)

class VioletButton(pygame.sprite.Sprite):
    def __init__(self, game, selected):
        self.groups = game.all_sprites, game.button
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((2 * TILESIZE, 2 * TILESIZE))
        self.rect = self.image.get_rect()
        self.selected = selected
        self.x = 65
        self.y = 20
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

        if self.selected == True:
            self.image.fill(VIOLET)
        else:
            self.image.fill(LILAC)

class IndigoButton(pygame.sprite.Sprite):
    def __init__(self, game, selected):
        self.groups = game.all_sprites, game.button
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((2 * TILESIZE, 2 * TILESIZE))
        self.rect = self.image.get_rect()
        self.selected = selected
        self.x = 65
        self.y = 26.5
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

        if self.selected == True:
            self.image.fill(NOTINDIGO)
        else:
            self.image.fill(INDIGO)


class StartWave(pygame.sprite.Sprite):
    # this is similar to the above except it is placed at the very top and is much larger in size
    def __init__(self, game, selected):
        self.groups = game.all_sprites, game.button
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((14 * TILESIZE, 4 * TILESIZE))
        self.rect = self.image.get_rect()
        self.x = 65
        self.y = 2
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        self.selected = selected
        self.image.fill(TOMATO)

        if self.selected == True:
            self.image.fill(TOMATO)
        else:
            self.image.fill(REDORANGE)

