import pygame, variables

class Camera():
    def __init__(self, screen, x = 0, y = 0):
        self.x = x
        self.y = y
        self.screen = screen
        self.deltaMouse = pygame.mouse.get_pos()

    def update(self):
        if pygame.mouse.get_pressed()[2] == True:
            self.x -= self.deltaMouse[0] - pygame.mouse.get_pos()[0]
            self.y -= self.deltaMouse[1] - pygame.mouse.get_pos()[1]
        if self.x > 0: self.x = 0
        if self.y > 0: self.y = 0
        if self.x - variables.width < -(variables.game_map.width * variables.tile_size): self.x = -(variables.game_map.width * variables.tile_size - variables.width)
        if self.y - variables.height < -(variables.game_map.height * variables.tile_size): self.y = -(variables.game_map.height * variables.tile_size - variables.height)
        self.deltaMouse = pygame.mouse.get_pos()
    
    def draw(self, sprite, location, affected_by_camera = True):
        if affected_by_camera:
            self.screen.blit(sprite, (self.x + location[0], + self.y + location[1]))
        else:
            self.screen.blit(sprite, (location[0], location[1]))
        
