import pygame, os
from states.state import State
from constants import *
from objects.SquareShape import *

class T1(State):
    def __init__(self, game):
        State.__init__(self, game)
        tree = SquareShape(game,2, 2, 50, "tree.png")
        
        
    def update(self, actions):
        pass

    def render(self, display):
        display.fill((GREEN))
        self.game.draw_grid()
        