import pygame, load_sprites
from variables import *
from game_map import *
from grass import *
pygame.init()

game_map = Game_map(10, 10, camera)

fpsClock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((000, 000, 000))

    camera.update()
    game_map.update()
    
    pygame.display.update()
    fpsClock.tick(FPS)
    
pygame.quit()
