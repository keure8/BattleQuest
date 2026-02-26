import pygame
from constants import *
import os

# Base class for game objects
class SquareShape(pygame.sprite.Sprite):
    def __init__(self, game, grid_x, grid_y, length, png):
        super().__init__(self.containers)
        self.game = game
        
        self.grid_x = grid_x
        self.grid_y = grid_y

        pixel_x = grid_x * TILE_SIZE
        pixel_y = grid_y * TILE_SIZE
        self.position = pygame.Vector2(pixel_x, pixel_y)
        self.length = length
        self.png = png
        self.image = self.load_image()
        self.rect = self.image.get_rect(topleft=self.position)

    def draw(self):
        self.game.game_canvas.blit(self.image, self.position)

    def update(self, actions):
        # must override
        pass

    def load_image(self):
        try:
            image_path = os.path.join("assets", self.png)
            image = pygame.image.load(image_path).convert_alpha()
            return image
        except pygame.error as e:
            print(f"Error loading image: {e}")
            return None
    
    def get_hit(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.kill()