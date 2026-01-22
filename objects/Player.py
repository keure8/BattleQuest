import pygame
from objects.SquareShape import SquareShape
from constants import *

class Player(SquareShape):
    def __init__ (self, game, grid_x, grid_y, length, png):
        super().__init__(game, grid_x, grid_y, length, png)        
            
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
            if self.grid_x < 19:
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
            if self.grid_y < 14:
                self.grid_y += 1
                self.update_rect()
                for object in self.game.solid:
                    if self.rect.colliderect(object):
                        self.grid_y -= 1
        self.game.reset_keys()
    
    def update_rect(self):
        self.rect.x = self.grid_x * TILE_SIZE
        self.rect.y = self.grid_y * TILE_SIZE        