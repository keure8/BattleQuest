import os, pygame
from constants import *
from states.title import Title
from objects.SquareShape import SquareShape

class Game():
    def __init__(self):
        pygame.init()
        self.game_canvas = pygame.Surface((SCREEN_W, SCREEN_H))
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up": False, "down": False, "action1": False, "action2": False, "start": False}
        self.state_stack = []
        self.last_level = 0
        self.load_assets()
        self.load_states()
        self.drawable = pygame.sprite.Group()
        SquareShape.containers = (self.drawable,)

    def game_loop(self):
        while self.playing:
            self.get_events()
            self.update()
            self.render()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_a:
                    self.actions['left'] = True
                if event.key == pygame.K_d:
                    self.actions['right'] = True
                if event.key == pygame.K_w:
                    self.actions['up'] = True
                if event.key == pygame.K_s:
                    self.actions['down'] = True
                if event.key == pygame.K_p:
                    self.actions['action1'] = True
                if event.key == pygame.K_o:
                    self.actions['action2'] = True
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.actions['left'] = False
                if event.key == pygame.K_d:
                    self.actions['right'] = False
                if event.key == pygame.K_w:
                    self.actions['up'] = False
                if event.key == pygame.K_s:
                    self.actions['down'] = False
                if event.key == pygame.K_p:
                    self.actions['action1'] = False
                if event.key == pygame.K_o:
                    self.actions['action2'] = False
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = False

    def update(self):
        self.state_stack[-1].update(self.actions)

    def render(self):
        self.game_canvas.fill((0,0,0))
        self.state_stack[-1].render(self.game_canvas)
        self.drawable.draw(self.game_canvas)
        self.screen.blit(pygame.transform.scale(self.game_canvas,(SCREEN_W, SCREEN_H)), (0,0))
        pygame.display.flip()
    
    def draw_text(self, surface, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        #text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def load_assets(self):
        # Create pointers to directories
        self.assets_dir = os.path.join("assets")
        self.font_name = pygame.font.get_default_font()

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def draw_grid(self):
        #Draw vertical lines
        for x in range(0, SCREEN_W, TILE_SIZE):
            pygame.draw.line(self.game_canvas, BLACK, (x, 0), (x, SCREEN_H))
        #Draw horizontal lines
        for y in range(0, SCREEN_H, TILE_SIZE):
            pygame.draw.line(self.game_canvas, BLACK, (0, y), (SCREEN_W, y))

    