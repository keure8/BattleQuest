import pygame, os
from states.state import State
from constants import *
from objects.SquareShape import *
from objects.Player import Player

class T1(State):
    def __init__(self, game):
        State.__init__(self, game)
        tree = SquareShape(game,2, 2, 50, "tree.png")
        pc = Player(game, 5, 5, 50, "basicPlayer.png")
        
        
    def update(self, actions):
        pass

    def render(self, display):
        display.fill((GREEN))
        self.game.draw_grid()
        