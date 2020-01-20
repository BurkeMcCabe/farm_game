import pygame, camera, load_sprites
from variables import *

class Action():
    def __init__(self, action_number):
        self.action_number = action_number
    
    def update(self, total_actions):
        self.draw(total_actions)

    def draw(self, total_actions):
        camera.draw(sprites["action_background"], (((self.action_number * action_tile_size) - (total_actions * tile_size / 2)) + (width / 2), height - action_tile_size), False)
