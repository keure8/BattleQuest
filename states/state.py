import pygame
from constants import *
from objects.Player import Player

class State():
    def __init__(self, game):
        self.game = game
        self.prev_state = None
        self.action_box = None
        self.action_menu_state = "main"
        self.turn_box = None
        self.action_cursor_state = 0
        self.combatants = []
        self.game.roll_initiative(self.combatants)
        self.combatants.sort(key=lambda x: x.initiative, reverse=True)
        self.turn_cursor_state = 0
        self.current_turn = None
       
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
        self.turn_box = self.game.pop_box(901, 1, 100, 750)
        self.game.draw_text(self.turn_box, "Turn Order:", 10, WHITE, 5, 5)
        y_offset = 30
        for member in self.combatants:
            self.game.draw_text(self.turn_box, member.name, 10, WHITE, 15, y_offset)
            y_offset +=15
        self.game.draw_cursor(self.turn_box, 5, self.turn_cursor_state*15+30)
        self.game.game_canvas.blit(self.turn_box, (901, 1))

    def draw_action_box(self):
        self.action_box = self.game.pop_box(1, 651, 1001, 100)
        x_offset = 25
        cursor_x_offset = 102
        if self.current_turn.pc:
            if self.action_menu_state == "main":
                self.game.draw_text(self.action_box, self.current_turn.name, 10, WHITE, 10, 5)
                self.game.draw_text(self.action_box, f"Health: {self.current_turn.current_health} / {self.current_turn.max_health}", 10, WHITE, 100, 5)
                self.game.draw_text(self.action_box, f"Speed: {self.current_turn.current_speed}", 10, WHITE, 200, 5)
                for item in self.current_turn.menu_buttons:
                    self.game.draw_text(self.action_box, str(item), 10, WHITE, x_offset, 25)
                    x_offset += 100
            if self.action_menu_state == "actions":
                for item in self.current_turn.actions:
                    self.game.draw_text(self.action_box, str(item), 10, WHITE, x_offset, 25)
                    x_offset += 100
            self.game.draw_cursor(self.action_box, self.action_cursor_state*cursor_x_offset+5, 25)
        self.game.game_canvas.blit(self.action_box, (1, 651))

    def player_turn(self):
        if not self.current_turn.pc:
            return
        if self.current_turn.moving_mode:
            self.current_turn.move(self.game.actions)
        elif self.current_turn.targeting_mode:
            self.current_turn.get_targets(self.game.actions)
            if self.game.actions["start"]:
                targets = []
                for i in self.combatants:
                    if self.current_turn.target_indicator.rect.colliderect(i):
                        targets.append(i)
                for target in targets:
                    target.get_hit(1)
                self.current_turn.target_indicator.kill()
                self.game.reset_keys()
                self.current_turn.targeting_mode = False
                self.action_menu_state = "main"
                self.action_cursor_state = 0
            if self.game.actions["back"]:
                self.game.reset_keys()
                self.current_turn.target_indicator.kill()
                self.current_turn.targeting_mode = False
                self.action_menu_state = "main"
                self.action_cursor_state = 0
        else:
            if self.game.actions["right"]:
                if self.action_cursor_state < len(self.combatants[self.turn_cursor_state].menu_buttons)-1:
                    self.action_cursor_state += 1
                    self.game.reset_keys()
            if self.game.actions["left"]:
                if self.action_cursor_state > 0:
                    self.action_cursor_state -= 1
                    self.game.reset_keys()
            if self.game.actions["start"]:
                if self.action_cursor_state == 0 and self.action_menu_state == "main":
                    self.current_turn.moving_mode = True
                    self.game.reset_keys()
                if self.action_cursor_state == 1 and self.action_menu_state == "main":
                    self.action_menu_state = "actions"
                    self.action_cursor_state = 0
                    self.game.reset_keys()
                if self.action_cursor_state == 0 and self.action_menu_state == "actions":
                    self.current_turn.targeting_mode = True