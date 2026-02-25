import pygame
from objects.SquareShape import SquareShape
from constants import *
from objects.HitBox import HitBox

class Player(SquareShape):
    def __init__ (self, game, grid_x, grid_y, length, png):
        super().__init__(game, grid_x, grid_y, length, png)

        self.name = "Basic Player"
        self.pc = True
        self.moving_mode = False
        self.targeting_mode = False
        self.target_indicator = None
        self.start_x, self.start_y = self.grid_x, self.grid_y
        self.move_delay = 0
        self.max_health = 10
        self.current_health = 10
        self.dex_mod = 19
        self.initiative = 0
        self.max_speed = 3
        self.current_speed = 3
        self.menu_buttons = ["Move", "Actions", "Bonus Actions", "End Turn"]
        self.actions = ["Attack"]      
            
    def update(self, actions):
        screen_x = self.grid_x * TILE_SIZE
        screen_y = self.grid_y * TILE_SIZE
        self.position = (screen_x, screen_y)
        self.rect.topleft = self.position
    
    def move(self, actions):
        if self.move_delay > 0:
            self.move_delay -= 1
            return
        if actions["start"]:
            self.start_x, self.start_y = self.grid_x, self.grid_y
            self.moving_mode = False
            self.game.reset_keys()
            return
        if actions["back"]:
            # Reset to where we started the turn
            self.grid_x, self.grid_y = self.start_x, self.start_y
            self.update_rect()
            self.current_speed = self.max_speed
            self.moving_mode = False
            self.game.reset_keys()
            return
        if self.current_speed > 0:
            dx, dy = 0, 0
            if actions["left"] and self.grid_x > 0:
                dx = -1
            elif actions["right"] and self.grid_x < 17:
                dx = 1
            elif actions["up"] and self.grid_y > 0:
                dy = -1
            elif actions["down"] and self.grid_y < 12:
                dy = 1
            if dx != 0 or dy != 0:
                self.grid_x += dx
                self.grid_y += dy
                self.update_rect
                self.current_speed -= 1

                for obstacle in self.game.solid:
                    if self.rect.colliderect(obstacle.rect):
                        self.grid_x -= dx
                        self.grid_y -= dy
                        self.update_rect
                        self.current_speed += 1
                        break
                self.move_delay = 10
            
    
    def update_rect(self):
        self.rect.x = self.grid_x * TILE_SIZE
        self.rect.y = self.grid_y * TILE_SIZE

    def attack(self, actions):
        if self.target_indicator is None:
            self.target_indicator = HitBox(self.game, self.grid_x+1, self.grid_y, 50, 50)
        if actions["up"] and self.target_indicator.grid_y >= self.grid_y:
            self.target_indicator.grid_x = self.grid_x
            self.target_indicator.grid_y = self.grid_y - 1
        if actions["right"] and self.target_indicator.grid_x <= self.grid_x+1:
            self.target_indicator.grid_x = self.grid_x+1
            self.target_indicator.grid_y = self.grid_y
        if actions["down"] and self.target_indicator.grid_y <= self.grid_y:
            self.target_indicator.grid_x = self.grid_x
            self.target_indicator.grid_y = self.grid_y+1
        if actions["left"] and self.target_indicator.grid_x >= self.grid_x-1:
            self.target_indicator.grid_x = self.grid_x-1
            self.target_indicator.grid_y = self.grid_y