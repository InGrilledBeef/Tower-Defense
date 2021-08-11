# These are the settings/constants that will be used throughout the code

import pygame

# Colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREENBLUE = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
MENU_COLOUR = (218, 179, 88)
VIOLET = (238, 130, 238)
LILAC = (200, 162, 200)
REDORANGE = (255, 69, 0)
TOMATO = (255, 99, 71)
INDIGO = (29, 0, 51)
NOTINDIGO = (129, 0, 151)


# Settings
TITLE = 'Tower Defense Game'
WIDTH = 1280
HEIGHT = 672    # 768 -> 672
BGCOLOUR = MENU_COLOUR
FPS = 60
ICON = pygame.image.load('TDLogo.png')

TILESIZE = 16
GRIDWIDTH = (WIDTH - 256) / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE