import pygame
from constants import *

class State():
    def __init__(self, game):
        self.game = game
        self.prev_state = None
        self.combatants = []
        self.game.roll_initiative(self.combatants)
        self.combatants.sort(key=lambda x: x.initiative, reverse=True)
       
    def update(self, delta_time, actions):
        pass
    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()

    def draw_grid(self):
        #Draw vertical lines
        for x in range(0, SCREEN_W, TILE_SIZE):
            pygame.draw.line(self.game.game_canvas, BLACK, (x, 0), (x, SCREEN_H))
        #Draw horizontal lines
        for y in range(0, SCREEN_H, TILE_SIZE):
            pygame.draw.line(self.game.game_canvas, BLACK, (0, y), (SCREEN_W, y))

    def draw_turn_box(self):
        turn_box = self.game.pop_box(901, 1, 100, 750)
        self.game.draw_text(turn_box, "Turn Order:", 10, WHITE, 50, 10)
        y_offset = 30
        for member in self.combatants:
            self.game.draw_text(turn_box, member.name, 10, WHITE, 50, y_offset)
            y_offset +=15
        self.game.game_canvas.blit(turn_box, (901, 1))

    def draw_action_box(self):
        action_box = self.game.pop_box(1, 651, 1001, 100)
        x_offset = 50
        if self.current_turn.pc:
            self.game.draw_text(action_box, self.current_turn.name, 10, WHITE, 50, 5)
            self.game.draw_text(action_box, f"Health: {self.current_turn.current_health} / {self.current_turn.max_health}", 10, WHITE, 200, 5)
            for item in self.current_turn.menu_buttons:
                self.game.draw_text(action_box, str(item), 10, WHITE, x_offset, 25)
                x_offset += 100
        self.game.game_canvas.blit(action_box, (1, 651))
