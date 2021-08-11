# Tower Defense Game
# Code by Ingrid Qin
# 2020/01/20
# main.py contains the main class Game which runs the game
# runs subclasses, methods

import pygame
import sys
import random
from os import path
from settings import *
from mobs import *
from tilemap import *
from menu import *
from towers import *


class Game:
    # Constructor (init func)
    def __init__(self):
        # Initialize pygame and pygame's fonts
        # create screen, set title of game to "Tower Defense Game," set icon/logo of game to preset image
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)

        # These are some constants that will be used in parts of the code
        self.lives = 50
        self.money = 200
        self.bluet_price = 75
        self.violett_price = 140
        self.indigot_price = 270

        # Runs the load_data() method
        self.load_data()

        # Initialize pygame's built in time/clock function
        self.clock = pygame.time.Clock()

        # Some lists defined to store the tower's colour, letter based on tile map, and position
        self.tower_colour = []
        self.tower_letter = []
        self.all_positions = []

        # Counters that will be used to deal with each button's functions
        self.wave_click = 0
        self.blueClick_num = 0
        self.violetClick_num = 0
        self.indigoClick_num = 0

        # When these turn True, specific text is displayed accordingly
        self.blue_info = False
        self.violet_info = False
        self.indigo_info = False
        self.game_over = False

    def load_data(self):
        game_folder = path.dirname(__file__)
        # Converts txt file to an actual playable map
        self.map = Map(path.join(game_folder, 'map1.txt'))

    def newmob(self):
        # when this function is called, a new mob is spawned
        self.mob = Mob()
        self.mobs.add(self.mob)

    def start_wave(self):
        # new mobs are generated when "Generate Mob" button is clicked
        # the number of mobs that spawn can range between 4 to 8 (usually with some overlapping)
        num_mobs = random.randint(4, 8)
        if self.wave_click == 1:
            for i in range(num_mobs):
                self.newmob()
            self.wave_click = 0

        # The button is REDORANGE when there is no mobs shown on the screen
        if not self.mobs:
            StartWave(self, False)

    def new(self):
        # In this function, sprites and sprite groups are called and defined
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.side_menu = pygame.sprite.Group()
        self.button = pygame.sprite.Group()
        self.towers = pygame.sprite.Group()
        self.grass = pygame.sprite.Group()
        self.base = pygame.sprite.Group()
        self.spots = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.startwave = StartWave(self, False)

        # enumerate: Number, Object
        # takes the tile map and makes objects based on it
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '.':
                    Grass(self, col, row)
                if tile == '2':
                    Base(self, col, row)

                # Since each spot has its own letter following the alphabet,
                # it is easier to use a for loop and generate the images based on the letter's ASCII values
                # a -> z
                for spot in range(97, 123):
                    if tile == chr(spot):
                        Spots(self, col, row)

                # A -> Z (this is the most genius thing I have ever done in my life)
                for spot in range(65, 91):
                    if tile == chr(spot):
                        Spots(self, col, row)

            # This is where the side menu and buttons are defined
            SideMenu(self, 64, 0)
            self.btns = [BlueButton(self, False), VioletButton(self, False), IndigoButton(self, False)]

    def collide(self):
        # This function deals with collisions
        # when the mobs group collide with the bullets group, the mob is killed by the bullet remains alive
        hits = pygame.sprite.groupcollide(self.mobs, self.bullets, True, False)

        # when the mobs reach the base, the mob is killed but the base remains alive
        self.groupcollide = pygame.sprite.groupcollide(self.mobs, self.base, True, False)
        path_end = self.groupcollide

        # Every time the user kills a mob, they gain $1
        # However, every time the mob reaches the base, the user loses a life
        for hit in hits:
            self.money += 1

        for c in path_end:
            self.lives -= 1

        if self.lives <= 0:
            self.lives = 0
            self.game_over = True

    def run(self):
        # Main loop. Runs the draw, update, events, start_wave, and collide functions.
        # self.clock.tick(FPS) is there to make sure the loop runs at 60 frames per second
        self.running = True
        while self.running:
            self.clock.tick(FPS) / 1000
            self.draw()
            self.update()
            self.events()
            self.start_wave()
            self.collide()

    def quit(self):
        # this function helps the user exit the game smoothly
        pygame.quit()
        sys.exit()

    def update(self):
        # Calls the update functions in the mobs, all_sprites, and bullets sprite groups
        self.mobs.update()
        self.all_sprites.update()
        self.bullets.update()

    def draw_grid(self):
        # This function draw the grid that appears on the screen
        # All the vertical lines
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        # All the horizontal lines
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # this function draws all of the sprites and blits it onto the screen
        self.screen.fill(BGCOLOUR)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        self.side_menu.draw(self.screen)
        self.button.draw(self.screen)
        self.bullets.draw(self.screen)
        self.towers.draw(self.screen)
        self.mobs.draw(self.screen)
        self.text()

        pygame.display.flip()

    def events(self):
        # this part deals with what the user is able to control
        for event in pygame.event.get():
            # if the user click the x in the top left corner, the quit function runs
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # gets mouse position in 2 different variables
                x, y = pygame.mouse.get_pos()
                self.button_press(x, y)
                self.wave_start(x, y)

    def wave_start(self, x, y):
        # generating new mobs costs 2 dollars.
        # This if statement only runs if the user has selected the "Generate Mobs" button
        if self.wave_click == 0 and self.money - 1 >= 0:
            if (x >= 65 * TILESIZE and x <= 79 * TILESIZE) and (y >= 2 * TILESIZE and y <= 6 * TILESIZE):
                StartWave(self, True)
                self.wave_click = 1
                self.money -= 2

        if self.money <= 0:
            self.money = 0

    def button_press(self, x, y):
        # this function deals with the tower buttons
        # If the user clicked on the button, the tower_place() function is called
        # and the price of the tower is subtracted from the total amount
        if self.blueClick_num == 1:
            self.tower_place(BLUE, x, y)
            self.money -= self.bluet_price
            self.blueClick_num += 1

        if self.violetClick_num == 1:
            self.tower_place(VIOLET, x, y)
            self.money -= self.violett_price
            self.violetClick_num += 1

        if self.indigoClick_num == 1:
            self.tower_place(INDIGO, x, y)
            self.money -= self.indigot_price
            self.indigoClick_num += 1


        # when the user clicks the button, before the above occurs, the button changes colours
        # and information about the specific tower is displayed
        if self.blueClick_num == 0 and (self.money - self.bluet_price) >= 0:
            if (x >= 65 * TILESIZE and y <= 67 * TILESIZE) and (y >= 14 * TILESIZE and y <= 16 * TILESIZE):
                BlueButton(self, True)
                self.blue_info = True
                self.blueClick_num += 1

        if self.violetClick_num == 0 and (self.money - self.violett_price) >= 0:
            if (x >= 65 * TILESIZE and y <= 67 * TILESIZE) and (y >= 20 * TILESIZE and y <= 22 * TILESIZE):
                VioletButton(self, True)
                self.violet_info = True
                self.violetClick_num += 1

        if self.indigoClick_num == 0 and (self.money - self.indigot_price) >= 0:
            if (x >= 65 * TILESIZE and y <= 67 * TILESIZE) and (y >= 26 * TILESIZE and y <= 28.5 * TILESIZE):
                IndigoButton(self, True)
                self.indigo_info = True
                self.indigoClick_num += 1

        # as a final step, when the tower is placed, everything is set back to their default values
        if self.blueClick_num == 2:
            BlueButton(self, False)
            self.blue_info = False
            self.blueClick_num = 0

        if self.violetClick_num == 2:
            VioletButton(self, False)
            self.violet_info = False
            self.violetClick_num = 0

        if self.indigoClick_num == 2:
            IndigoButton(self, False)
            self.indigo_info = False
            self.indigoClick_num = 0

    def tower_shoot(self, colour, col, row, letter):
        # this function adds the parameters into the lists defined in the init function
        # and generates a new bullet
        position = []
        self.tower_colour.append(colour)
        position.append(col)
        position.append(row)
        self.tower_letter.append(letter)
        self.all_positions.append(position)
        self.bullet = Bullet(col, row, letter, colour)
        self.bullets.add(self.bullet)

    def tower_place(self, colour, x, y):
        # this function uses the position the user clicked
        # and colour of the button the user clicked to determine what type of tower should be placed.
        # Tile map is used to identify the exact position, and the Tower class is called

        temp = 0
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                # top row
                if 64 <= y <= 96:
                    if 48 <= x <= 80:
                        if tile == 'a':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 112 <= x <= 144:
                        if tile == 'b':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 256 <= x <= 288:
                        if tile == 'q':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 320 <= x <= 352:
                        if tile == 'r':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 384 <= x <= 416:
                        if tile == 's':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 544 <= x <= 576:
                        if tile == 'H':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 608 <= x <= 640:
                        if tile == 'I':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 672 <= x <= 704:
                        if tile == 'J':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1

                # Columns excluding top and bottom
                # First column
                if 176 <= x <= 208:
                    if 192 <= y <= 224:
                        if tile == 'd':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 256 <= y <= 288:
                        if tile == 'e':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 320 <= y <= 352:
                        if tile == 'f':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 384 <= y <= 416:
                        if tile == 'g':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 448 <= y <= 480:
                        if tile == 'h':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 512 <= y <= 544:
                        if tile == 'i':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                # Second column
                if 320 <= x <= 352:
                    if 192 <= y <= 224:
                        if tile == 'p':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 256 <= y <= 288:
                        if tile == 'o':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 320 <= y <= 352:
                        if tile == 'n':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 384 <= y <= 416:
                        if tile == 'm':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 448 <= y <= 480:
                        if tile == 'l':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 512 <= y <= 544:
                        if tile == 'k':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1

                # Third column
                if 464 <= x <= 496:
                    if 192 <= y <= 224:
                        if tile == 'u':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 256 <= y <= 288:
                        if tile == 'v':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 320 <= y <= 352:
                        if tile == 'w':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 384 <= y <= 416:
                        if tile == 'x':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 448 <= y <= 480:
                        if tile == 'y':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 512 <= y <= 544:
                        if tile == 'z':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1

                # Fourth column
                if 608 <= x <= 640:
                    if 192 <= y <= 224:
                        if tile == 'G':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 256 <= y <= 288:
                        if tile == 'F':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 320 <= y <= 352:
                        if tile == 'E':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 384 <= y <= 416:
                        if tile == 'D':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 448 <= y <= 480:
                        if tile == 'C':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 512 <= y <= 544:
                        if tile == 'B':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1

                # Fifth column
                if 752 <= x <= 784:
                    if 192 <= y <= 224:
                        if tile == 'L':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 256 <= y <= 288:
                        if tile == 'M':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 320 <= y <= 352:
                        if tile == 'N':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 384 <= y <= 416:
                        if tile == 'O':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 448 <= y <= 480:
                        if tile == 'P':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 512 <= y <= 544:
                        if tile == 'Q':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1

                # Sixth column
                if 800 <= x <= 832:
                    if 192 <= y <= 224:
                        if tile == 'W':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 256 <= y <= 288:
                        if tile == 'V':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 320 <= y <= 352:
                        if tile == 'U':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 384 <= y <= 416:
                        if tile == 'T':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 448 <= y <= 480:
                        if tile == 'S':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 512 <= y <= 544:
                        if tile == 'R':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1

                # Second Row
                if 128 <= y <= 160:
                    if 176 <= x <= 208:
                        if tile == 'c':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 464 <= x <= 496:
                        if tile == 't':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 752 <= x <= 784:
                        if tile == 'K':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 800 <= x <= 832:
                        if tile == 'X':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1

                # Last Row
                if 576 <= y <= 608:
                    if 320 <= x <= 352:
                        if tile == 'j':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1
                    if 608 <= x <= 640:
                        if tile == 'A':
                            Tower(self, True, col, row, colour)
                            if temp == 3:
                                self.tower_shoot(colour, col, row, tile)
                            temp += 1

    def text(self):
        # this function displays all the text that appear on the screen when called
        font = pygame.font.SysFont('Comic Sans MS', 24)
        gen_mob = font.render("Generate Mobs", True, (BLUE))
        self.screen.blit(gen_mob, (66.5 * TILESIZE, 2.5 * TILESIZE))
        tfont = pygame.font.SysFont('Comic Sans MS', 18)
        blue_t = tfont.render("Blue Tower", True, (BLACK))
        self.screen.blit(blue_t, (68 * TILESIZE, 14 * TILESIZE))
        violet_t = tfont.render("Violet Tower", True, (BLACK))
        self.screen.blit(violet_t, (68 * TILESIZE, 20 * TILESIZE))
        indigo_t = tfont.render("Indigo Tower", True, (BLACK))
        self.screen.blit(indigo_t, (68 * TILESIZE, 26.5 * TILESIZE))
        money_f = font.render("Money: $" + str(self.money), True, (BLACK))
        self.screen.blit(money_f, (65 * TILESIZE, 7 * TILESIZE))
        life_f = font.render("Lives: " + str(self.lives), True, (BLACK))
        self.screen.blit(life_f, (65 * TILESIZE, 10 * TILESIZE))
        font_over = pygame.font.SysFont('freesansbold.ttf', 100)
        if self.game_over == True:
            over_font = font_over.render("Game Over", True, (BLACK))
            self.screen.blit(over_font, (24 * TILESIZE, HEIGHT / 2))
        if self.blue_info == True:
            blue_c = font.render("Cost: $" + str(self.bluet_price), True, (BLACK))
            self.screen.blit(blue_c, (65 * TILESIZE, 31 * TILESIZE))
            blue_s = font.render("Speed: 20", True, (BLACK))
            self.screen.blit(blue_s, (65 * TILESIZE, 36 * TILESIZE))
        if self.violet_info == True:
            violet_c = font.render("Cost: $" + str(self.violett_price), True, (BLACK))
            self.screen.blit(violet_c, (65 * TILESIZE, 31 * TILESIZE))
            violet_s = font.render("Speed: 40", True, (BLACK))
            self.screen.blit(violet_s, (65 * TILESIZE, 36 * TILESIZE))
        if self.indigo_info == True:
            indigo_c = font.render("Cost: $" + str(self.indigot_price), True, (BLACK))
            self.screen.blit(indigo_c, (65 * TILESIZE, 31 * TILESIZE))
            indigo_s = font.render("Speed: 80", True, (BLACK))
            self.screen.blit(indigo_s, (65 * TILESIZE, 36 * TILESIZE))

# this runs the run function and the new function in a loop. If the run function is exited, the while loop is exited
# and the entire code stops running
g = Game()
while True:
    g.new()
    g.run()

pygame.quit()
