import pygame
from objects.SquareShape import SquareShape
from constants import *

class Player(SquareShape):
    def __init__ (self, game, grid_x, grid_y, length, png):
        super().__init__(game, grid_x, grid_y, length, png)

        self.name = "Basic Player"
        self.pc = True
        self.max_health = 10
        self.current_health = 10
        self.dex_mod = 19
        self.initiative = 0
        self.menu_buttons = ["Move", "Actions", "Bonus Actions", "End Turn"]
        self.actions = ["attack"]      
            
    def update(self, actions):
        self.move(actions)
        screen_x = self.grid_x * TILE_SIZE
        screen_y = self.grid_y * TILE_SIZE
        self.position = (screen_x, screen_y)
        self.rect.topleft = self.position
    
    def move(self, actions):
        if actions["left"]:
            if self.grid_x > 0:
                self.grid_x -= 1
                self.update_rect()
                for object in self.game.solid:
                    if self.rect.colliderect(object):
                        self.grid_x += 1
        if actions["right"]:
            if self.grid_x < 17:
                self.grid_x += 1
                self.update_rect()
                for object in self.game.solid:
                    if self.rect.colliderect(object):
                        self.grid_x -= 1
        if actions["up"]:
            if self.grid_y > 0:
                self.grid_y -= 1
                self.update_rect()
                for object in self.game.solid:
                    if self.rect.colliderect(object):
                        self.grid_y += 1
        if actions["down"]:
            if self.grid_y < 12:
                self.grid_y += 1
                self.update_rect()
                for object in self.game.solid:
                    if self.rect.colliderect(object):
                        self.grid_y -= 1
        self.game.reset_keys()
    
    def update_rect(self):
        self.rect.x = self.grid_x * TILE_SIZE
        self.rect.y = self.grid_y * TILE_SIZE

    def basic_attack(self, target):
        target.get_hit(1)
