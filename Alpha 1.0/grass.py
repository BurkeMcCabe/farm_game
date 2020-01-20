import pygame
from variables import *
class Grass():
    def __init__(self, x, y, size, camera):
        self.x = x
        self.y = y
        self.size = size
        self.sprite = sprites["Grass"]
        self.camera = camera
        
    def update(self):
        self.draw()
        
    def draw(self):
        self.camera.draw(self.sprite, (self.x, self.y))
        
