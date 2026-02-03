import pygame, os
from states.state import State
from constants import *
from states.T1 import T1

class Tutorial_Town(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.T_Town_Img = pygame.image.load(os.path.join(self.game.assets_dir, "Tutorial_Town.png"))
        
    def update(self, actions):
        if actions["start"]:
            if self.game.last_level == 0:
                new_state = T1(self.game)
                new_state.enter_state()

    def render(self, display):
        display.blit(self.T_Town_Img, (0,0))
        self.pop_box("Hello World!", 20, WHITE, 400, 130, 150, 30)