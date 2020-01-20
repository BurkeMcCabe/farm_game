import load_sprites, camera, pygame

ACCEPTED_IMAGE_FORMATS = ["png", "jpg", "bmp"]
FPS = 60


width, height = 1280, 690
tile_size = 64
sprites = load_sprites.load_sprites(tile_size, ACCEPTED_IMAGE_FORMATS)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
camera = camera.Camera(screen)
