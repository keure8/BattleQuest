import pygame, os
from states.state import State
from constants import *
from objects.SquareShape import *
from objects.Player import Player
from objects.Young_Buck import Young_Buck

class T1(State):
    def __init__(self, game):
        State.__init__(self, game)
        tree = SquareShape(game,2, 2, 50, "tree.png")
        pc = Player(game, 5, 5, 50, "basicPlayer.png")
        deer = Young_Buck(game, 7, 7, 50, "deer.png")
        self.combatants = [pc, deer]
        self.game.roll_initiative(self.combatants)
        self.combatants.sort(key=lambda x: x.initiative, reverse=True)
        turn_index = 0
        self.current_turn = self.combatants[turn_index]  
        
    def update(self, actions):
        pass

    def render(self, display):
        display.fill((GREEN))
        self.draw_grid()
        self.draw_turn_box()
        self.draw_action_box()