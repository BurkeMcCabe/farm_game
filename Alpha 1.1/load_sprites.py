import pygame, os
pygame.init()

def load_sprites(tile_size, accepted_image_formats):
    path = os.path.abspath("load_sprites.py").replace("load_sprites.py", "")
    sprite_paths = []
    names = []
    
    for(image_path, image_dirs, image_files) in os.walk(path):
        image_path.replace(path, "")
        for file in image_files:
            sprite_paths.append(image_path + r"\-".replace("-", "") + file)
            names.append(file)

    sprites = {}
    offset = 0
    can_offset = True
    
    for sprite_path in range(len(sprite_paths)):
        can_offset = True
        for accepted_image_format in accepted_image_formats:
            if (sprite_paths[sprite_path][-(len(accepted_image_format)):] == accepted_image_format):
                sprites[names[sprite_path].replace("." + accepted_image_format, "")] = pygame.image.load(sprite_paths[sprite_path])
                sprites[names[sprite_path].replace("." + accepted_image_format, "")] = pygame.transform.scale(sprites[names[sprite_path].replace("." + accepted_image_format, "")], (tile_size, tile_size))
            elif can_offset:
                offset += 1
            can_offset = False
    return sprites
