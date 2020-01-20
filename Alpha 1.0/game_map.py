import pygame
from grass import *
from variables import *

class Game_map():
    def __init__(self, width, height, camera):
        self.width = width
        self.height = height
        self.camera = camera
        self.map = [[]]
        for x_tile in range(self.width):
            for y_tile in range(self.height):
                self.map[x_tile].append(Grass(x_tile * tile_size, y_tile * tile_size, tile_size, camera))
            self.map.append([])

    def update(self):
        for x_tile in range(self.width):
            for y_tile in range(self.height):
                self.map[x_tile][y_tile].update()

    def draw(self):
        pass
        
