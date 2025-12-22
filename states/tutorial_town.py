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
        self.game.draw_text(display, "Today is the day my child.", 15, BLACK, SCREEN_W/3, SCREEN_H/3)
        self.game.draw_text(display, "Your quest to learn the ways of the world.", 15, BLACK, SCREEN_W/3, SCREEN_H/3+20)
        self.game.draw_text(display, "Take this sword and hunt.", 15, BLACK, SCREEN_W/3, SCREEN_H/3+40)
        self.game.draw_text(display, "Press Start To Continue", 10, WHITE, SCREEN_W/3, SCREEN_H/3+60)