import pygame, load_sprites
from variables import *
from grass import *
from actions import *
pygame.init()

fpsClock = pygame.time.Clock()

actions = Actions(4)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                actions.action_selected -= 1
            elif event.button == 5:
                actions.action_selected += 1
    
    screen.fill((000, 000, 000))
    
    camera.update()
    game_map.update()
    actions.update()
    
    pygame.display.update()
    fpsClock.tick(FPS)
    
pygame.quit()
