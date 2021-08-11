# tilemap.py deals with the background of the game

import pygame
from settings import *
from tilemap import *


class Map:
    def __init__(self, filename):
        # list to store data from tile map
        self.data = []
        # rt = read only
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE


class Grass(pygame.sprite.Sprite):
    # this subclass makes all of the green blocks that appear on the screen
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.grass
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class SideMenu(pygame.sprite.Sprite):
    # this subclass makes the side menu that appears on the screen
    def __init__(self, game, x, y):
        self.groups = game.side_menu
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((16 * TILESIZE, 48 * TILESIZE))
        self.image.fill(MENU_COLOUR)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Base(pygame.sprite.Sprite):
    # this subclass generates the base that the mobs are heading towards that appears on the screen
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.base
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Spots(pygame.sprite.Sprite):
    # this subclass generates the spots that the towers can be placed on
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.spots
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
