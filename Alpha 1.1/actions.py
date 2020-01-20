import pygame
from action import *

class Actions():
    def __init__(self, action_amount):
        self.actions = []
        for action in range(action_amount):
            self.actions.append(Action(action))
        self.action_selected = 0

    def update(self):
        for action in self.actions:
            action.update(len(self.actions))
        if self.action_selected < 0 : self.action_selected = action_amount - 1
        elif self.action_selected + 1 > 4 : self.action_selected = 0
        self.draw()

    def draw(self):
        camera.draw(sprites["action_selector"], (self.action_selected * action_tile_size + width / 2 - len(self.actions) * action_tile_size / 2 , height - action_tile_size), False)
