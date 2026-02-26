import pygame
from constants import *
import os

class HitBox(pygame.sprite.Sprite):
    def __init__(self, game, grid_x, grid_y, width, height):
        super().__init__(self.containers)
        self.game = game

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((255, 255, 0, 150))
        
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.rect = self.image.get_rect()
        self.update_postion()
    
    def update_postion(self):
        self.rect.topleft = (self.grid_x * TILE_SIZE, self.grid_y * TILE_SIZE)

    def update(self, actions):
        self.update_postion()
