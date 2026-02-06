import pygame
from objects.SquareShape import SquareShape
from constants import *

class Enemy(SquareShape):
    def __init__ (self, game, grid_x, grid_y, length, png):
        super().__init__(game, grid_x, grid_y, length, png)        
            
    def update(self, actions):
        screen_x = self.grid_x * TILE_SIZE
        screen_y = self.grid_y * TILE_SIZE
        self.position = (screen_x, screen_y)
        self.rect.topleft = self.position

    def get_hit(self, damage):
        self.health -= damage