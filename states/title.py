from states.state import State
from constants import *
from states.tutorial_town import Tutorial_Town

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, actions):
        if actions["start"]:
            new_state = Tutorial_Town(self.game)
            new_state.enter_state()
            self.game.reset_keys()

    def render(self, display):
        display.fill((BLACK))
        self.game.draw_text(display, "Battle Quest", 20,  RED, SCREEN_W/2-70, SCREEN_H/2)
        self.game.draw_text(display, "Press Enter To Start", 10, WHITE, SCREEN_W/2-55, SCREEN_H/2+20)