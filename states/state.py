import pygame
from constants import *

class State():
    def __init__(self, game):
        self.game = game
        self.prev_state = None

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

    def pop_box(self, message, size, color, x, y, w, h):
        pop_surface = pygame.Surface((w, h))
        pop_rect = pop_surface.get_rect()
        pop_rect.topleft = (x,y)
        pop_surface.fill(BLACK)
        font = pygame.font.Font(self.game.font_name, size)
        text_surface = font.render(message, True, color)
        #text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (2, 2)
        pop_surface.blit(text_surface, text_rect)
        self.game.game_canvas.blit(pop_surface, pop_rect)