import pygame

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
        self.deltaMouse = pygame.mouse.get_pos()
    
    def draw(self, sprite, location):
        self.screen.blit(sprite, (self.x + location[0], + self.y + location[1]))
        
