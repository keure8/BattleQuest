import pygame
from objects.SquareShape import SquareShape
from objects.Enemy import Enemy
from constants import *

class Young_Buck(Enemy):
    def __init__ (self, game, grid_x, grid_y, length, png):
        super().__init__(game, grid_x, grid_y, length, png)
        
        self.name = "Young Buck"
        self.pc = False
        self.health = 1
        self.dex_mod = 1
        self.initiative = 0