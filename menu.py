import pygame
import os
from constants import *

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = DISPLAY_W / 2, DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
            
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(BLACK)
            self.game.draw_text('Battle Quest', 20, DISPLAY_W / 2, DISPLAY_H / 2 - 20)
            self.game.draw_text('Press ENTER To Start', 10, DISPLAY_W / 2, DISPLAY_H / 2)
            self.blit_screen()

    def check_input(self):
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.curr_menu = self.game.character_select
            self.run_display = False

class CharacterSelect(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "CharacterSelect"
        self.offset = -20
        self.cursor_rect.midtop = (DISPLAY_W / 4 + self.offset, 40)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(BLACK)
            self.game.draw_text('Character Select', 20, DISPLAY_W / 2, 10)
            self.game.draw_text("Basic", 10, DISPLAY_W / 4, 40)
            self.game.draw_image('basicPlayer.png', DISPLAY_W / 4, 70)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.START_KEY:
            if self.state == 'CharacterSelect':
                self.game.playing = True
            self.run_display = False
        