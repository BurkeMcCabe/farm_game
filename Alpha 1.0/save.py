import pygame, os
pygame.init()

def load_sprites(tile_size, accepted_image_formats):
    path = os.path.abspath("load_sprites.py").replace("load_sprites.py", "")
    sprite_paths = []

    for(image_path, image_dirs, image_files) in os.walk(path):
        image_path.replace(path, "")
        for file in image_files:
            sprite_paths.append(image_path + r"\-".replace("-", "") + file)

    sprites = []
    offset = 0
    can_offset = True
    
    for sprite_path in sprite_paths:
        can_offset = True
        for accepted_image_format in accepted_image_formats:
            if (sprite_path[-(len(accepted_image_format)):] == accepted_image_format):
                sprites.append(pygame.image.load(sprite_path))
                sprites[sprite_paths.index(sprite_path) - offset] = pygame.transform.scale(sprites[sprite_paths.index(sprite_path) - offset], (tile_size, tile_size))
            elif can_offset:
                offset += 1
            can_offset = False
    return sprites

def find_sprite(sprite_name):
    pass
