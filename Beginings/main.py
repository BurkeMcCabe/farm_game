import pygame, sys

from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1280, 960
screen = pygame.display.set_mode((width, height))

camera_x, camera_y = 0,0
tile_size = 64
deltaMouse = pygame.mouse.get_pos()

running = True

font = pygame.font.Font(None, 40)

action_selection = 0

inventory = []
inventory_amt = []

money = 10

clicked = False
held = False

action_size = tile_size

starting_tick = 0

grass_sprite = pygame.image.load("Grass.png")
grass_sprite = pygame.transform.scale(grass_sprite, (tile_size, tile_size))
tilled_soil_sprite = pygame.image.load("Tilled_Soil.png")
tilled_soil_sprite = pygame.transform.scale(tilled_soil_sprite, (tile_size, tile_size))
tilled_soil_top_sprite = pygame.image.load("Tilled_Soil_Top.png")
tilled_soil_top_sprite = pygame.transform.scale(tilled_soil_top_sprite, (tile_size, tile_size))

hoe_sprite = pygame.image.load("Hoe.png")
hoe_sprite = pygame.transform.scale(hoe_sprite, (tile_size, tile_size))
wheat_seed_sprite = pygame.image.load("wheat_seed.png")
wheat_seed_sprite = pygame.transform.scale(wheat_seed_sprite, (tile_size, tile_size))
potato_seed_sprite = pygame.image.load("potato_seed.png")
potato_seed_sprite = pygame.transform.scale(potato_seed_sprite, (tile_size, tile_size))
hand_sprite = pygame.image.load("Hand.png")
hand_sprite = pygame.transform.scale(hand_sprite, (tile_size, tile_size))

wheat_stage_1_sprite = pygame.image.load("Wheat/Wheat_stage_1.png")
wheat_stage_1_sprite = pygame.transform.scale(wheat_stage_1_sprite, (tile_size, tile_size))
wheat_stage_2_sprite = pygame.image.load("Wheat/Wheat_stage_2.png")
wheat_stage_2_sprite = pygame.transform.scale(wheat_stage_2_sprite, (tile_size, tile_size))
wheat_stage_3_sprite = pygame.image.load("Wheat/Wheat_stage_3.png")
wheat_stage_3_sprite = pygame.transform.scale(wheat_stage_3_sprite, (tile_size, tile_size))
wheat_stage_4_sprite = pygame.image.load("Wheat/Wheat_stage_4.png")
wheat_stage_4_sprite = pygame.transform.scale(wheat_stage_4_sprite, (tile_size, tile_size))
wheat_stage_5_sprite = pygame.image.load("Wheat/Wheat_stage_5.png")
wheat_stage_5_sprite = pygame.transform.scale(wheat_stage_5_sprite, (tile_size, tile_size))
wheat_stage_6_sprite = pygame.image.load("Wheat/Wheat_stage_6.png")
wheat_stage_6_sprite = pygame.transform.scale(wheat_stage_6_sprite, (tile_size, tile_size))
wheat_stage_7_sprite = pygame.image.load("Wheat/Wheat_stage_7.png")
wheat_stage_7_sprite = pygame.transform.scale(wheat_stage_7_sprite, (tile_size, tile_size))
wheat_stage_8_sprite = pygame.image.load("Wheat/Wheat_stage_8.png")
wheat_stage_8_sprite = pygame.transform.scale(wheat_stage_8_sprite, (tile_size, tile_size))

potato_stage_1_sprite = pygame.image.load("Potato/Potato_stage_1.png")
potato_stage_1_sprite = pygame.transform.scale(potato_stage_1_sprite, (tile_size, tile_size))
potato_stage_2_sprite = pygame.image.load("Potato/Potato_stage_2.png")
potato_stage_2_sprite = pygame.transform.scale(potato_stage_2_sprite, (tile_size, tile_size))
potato_stage_3_sprite = pygame.image.load("Potato/Potato_stage_3.png")
potato_stage_3_sprite = pygame.transform.scale(potato_stage_3_sprite, (tile_size, tile_size))
potato_stage_4_sprite = pygame.image.load("Potato/Potato_stage_4.png")
potato_stage_4_sprite = pygame.transform.scale(potato_stage_4_sprite, (tile_size, tile_size))
potato_stage_5_sprite = pygame.image.load("Potato/Potato_stage_5.png")
potato_stage_5_sprite = pygame.transform.scale(potato_stage_5_sprite, (tile_size, tile_size))
potato_stage_6_sprite = pygame.image.load("Potato/Potato_stage_6.png")
potato_stage_6_sprite = pygame.transform.scale(potato_stage_6_sprite, (tile_size, tile_size))
potato_stage_7_sprite = pygame.image.load("Potato/Potato_stage_7.png")
potato_stage_7_sprite = pygame.transform.scale(potato_stage_7_sprite, (tile_size, tile_size))
potato_stage_8_sprite = pygame.image.load("Potato/Potato_stage_8.png")
potato_stage_8_sprite = pygame.transform.scale(potato_stage_8_sprite, (tile_size, tile_size))

class Plant():
    def update(self):
        self.stage = int((pygame.time.get_ticks() - self.starting_tick) / 1000 * self.max_stage / self.grow_time + 1)
        if self.stage > self.max_stage: self.stage = self.max_stage
        exec("self.sprite = %s" % (self.name + "_stage_" + str(self.stage) + "_sprite"))

class Wheat(Plant):
    def __init__(self):
        self.starting_tick = pygame.time.get_ticks()
        self.stage = 1
        self.max_stage = 8
        self.sprite_name = "wheat_stage_1_sprite"
        self.sprite = wheat_stage_1_sprite
        self.name = "wheat"
        self.cost = 1
        self.value = 2
        self.grow_time = 10

class Potato(Plant):
    def __init__(self):
        self.starting_tick = pygame.time.get_ticks()
        self.stage = 1
        self.max_stage = 8
        self.sprite_name = "potato_stage_1_sprite"
        self.sprite = potato_stage_1_sprite
        self.name = "potato"
        self.cost = 1
        self.value = 3
        self.grow_time = 13

def update_inventory():
    global money, clicked, held, starting_tick
    screen.blit(font.render("Inventory", False, (0, 255, 100)), (width - 200, 10))
    for item in range(len(inventory)):
        if pygame.mouse.get_pos()[0] >= width - 200 and pygame.mouse.get_pos()[1] >= (item + 1) * 40 and pygame.mouse.get_pos()[0] <= width - 200 + 190 and pygame.mouse.get_pos()[1] <= (item + 1) * 40  + 30:
            pygame.draw.rect(screen, (50, 50, 255), (width - 200, (item + 1) * 40, 190, 30))
            if pygame.mouse.get_pressed()[0] and inventory_amt[item] > 0 and (not clicked or held):
                if not clicked:
                    starting_tick = pygame.time.get_ticks()
                    clicked = True
                money += inventory[item].value
                inventory_amt[item] -= 1
            if not pygame.mouse.get_pressed()[0] and clicked == True:
                clicked = False
                held = False
            if pygame.time.get_ticks() - starting_tick >= 350 and clicked:
                held = True
        if inventory_amt[item] <= 0:
            del inventory[item]
            del inventory_amt[item]
            break
        screen.blit(font.render(inventory[item].name, False, (0, 200, 255)), (width - 200, (item + 1) * 40))
        screen.blit(font.render("x " + str(inventory_amt[item]), False, (0, 200, 255)), (width - 80, (item + 1) * 40))
        
def add_item(item):
    if item != None:
        for thing in range(len(inventory)):
            if type(item) == type(inventory[thing]):
                inventory_amt[thing] += 1
                return
            
        inventory.append(item)
        inventory_amt.append(1)
            

def remove_plant(location):
    if seed_layer[location[0]][location[1]] != None:
        plant = seed_layer[location[0]][location[1]]
        try:
            if plant.stage == plant.max_stage:
                seed_layer[location[0]][location[1]] = None
                return plant
        except:
            pass
        seed_layer[location[0]][location[1]] = None
        
    
def plant_seed(seed, location):
    global money
    if land_layer[location[0]][location[1]] == "tilled_soil" and money >= seed.cost:
        money -= seed.cost
        seed_layer[location[0]][location[1]] = seed

def update_action_selector(amt_of_actions):
    global action_selection
    screen.blit(hoe_sprite, (action_size * 0, height - action_size))
    screen.blit(wheat_seed_sprite, (action_size * 1, height - action_size))
    screen.blit(potato_seed_sprite, (action_size * 2, height - action_size))
    screen.blit(hand_sprite, (action_size * 3, height - action_size))
    pygame.draw.rect(screen, (100, 100, 0), (action_size * action_selection, height - action_size, action_size, action_size), 2)
    if pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[1] >= height - action_size and pygame.mouse.get_pos()[0] <= 4 * tile_size and pygame.mouse.get_pos()[1] <= height:
        pygame.draw.rect(screen, (200, 0, 0), (action_size * int(pygame.mouse.get_pos()[0] / action_size), height - action_size, action_size, action_size), 2)
        if pygame.mouse.get_pressed()[0]:
            action_selection = int(pygame.mouse.get_pos()[0] / action_size)

def till_soil(tile_coordinate):
    if not (pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[1] >= height - action_size and pygame.mouse.get_pos()[0] <= 4 * tile_size and pygame.mouse.get_pos()[1] <= height):
        land_layer[tile_coordinate[0]][tile_coordinate[1]] = "tilled_soil"

def calculate_rect(coordinates, tile_size):
    coordinates = list(coordinates)
    coordinates[0] = coordinates[0] * tile_size + camera_x
    coordinates[1] = coordinates[1] * tile_size + camera_y
    coordinates = tuple(coordinates)
    return coordinates
    
def create_layer(width, height, ground = None):
    layer = []
    for tiles_x in range(width):
        layer.append([])
        for tiles_y in range(height):
            layer[tiles_x].append(ground)
    return layer

def draw_land_layer(land_layer):
    for tiles_x in range(len(land_layer)):
        for tiles_y in range(len(land_layer[0])):
            if land_layer[tiles_x][tiles_y] == "grass":
                screen.blit(grass_sprite, (calculate_rect((tiles_x, tiles_y), tile_size)))
            elif land_layer[tiles_x][tiles_y] == "tilled_soil":
                if land_layer[tiles_x][tiles_y - 1] != "tilled_soil":
                    screen.blit(tilled_soil_top_sprite, (calculate_rect((tiles_x, tiles_y), tile_size)))
                else:
                    screen.blit(tilled_soil_sprite, (calculate_rect((tiles_x, tiles_y), tile_size)))

def draw_seed_layer(seed_layer):
    for tiles_x in range(len(seed_layer)):
        for tiles_y in range(len(seed_layer[0])):
            try:
                screen.blit(seed_layer[tiles_x][tiles_y].sprite, (calculate_rect((tiles_x, tiles_y), tile_size)))
            except:
                pass
                               
def find_tile_at_pixel(pixel_location, tile_size):
    tile_x = int((pixel_location[0] - camera_x) / tile_size)
    tile_y = int((pixel_location[1] - camera_y) / tile_size)
    if pixel_location[0] - camera_x < 0: tile_x += -1
    if pixel_location[1] - camera_y < 0: tile_y += -1
    
    return (tile_x, tile_y)

def draw_selector(tile_coordinates, tile_size):
    if find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)[0] >= 0 and find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)[1] >= 0 and find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)[0] <= len(land_layer) - 1 and find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)[1] <= len(land_layer[0]) - 1 and not (pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[1] >= height - action_size and pygame.mouse.get_pos()[0] <= 4 * tile_size and pygame.mouse.get_pos()[1] <= height):
        pygame.draw.rect(screen, (255, 255, 255), (tile_coordinates[0] * tile_size + camera_x, tile_coordinates[1] * tile_size + camera_y, tile_size, tile_size), 2)

land_layer = create_layer(50, 30, "grass")
seed_layer = create_layer(50, 30)

# Game loop
while (running):
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass
    
    # Update
    if pygame.mouse.get_pressed()[2] == True:
        camera_x -= deltaMouse[0] - pygame.mouse.get_pos()[0]
        camera_y -= deltaMouse[1] - pygame.mouse.get_pos()[1]
    if camera_x > 0: camera_x = 0
    if camera_y > 0: camera_y = 0
    if camera_x - width < -(len(land_layer) * tile_size): camera_x = -(len(land_layer) * tile_size - width)
    if camera_y - height < -(len(land_layer[0]) * tile_size): camera_y = -(len(land_layer[0]) * tile_size - height)
    deltaMouse = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0] == True and find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)[0] >= 0 and find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)[1] >= 0 and find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)[0] <= len(land_layer) - 1 and find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)[1] <= len(land_layer[0]) - 1:
        if action_selection == 0:      
            till_soil(find_tile_at_pixel(pygame.mouse.get_pos(), tile_size))
        elif action_selection == 1 and seed_layer[find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)[0]][find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)[1]] == None:
            plant_seed(Wheat(), (find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)))
        elif action_selection == 2 and seed_layer[find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)[0]][find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)[1]] == None:
            plant_seed(Potato(), (find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)))
        elif action_selection == 3:
            add_item(remove_plant(find_tile_at_pixel(pygame.mouse.get_pos(), tile_size)))
            

    for row in seed_layer:
        for seed in row:
            try:
                seed.update()
            except:
                pass
    
    # Draw
    draw_land_layer(land_layer)
    draw_seed_layer(seed_layer)
    draw_selector(find_tile_at_pixel(pygame.mouse.get_pos(), tile_size), tile_size)
    update_action_selector(3)
    screen.blit(font.render("C = " + str(money), False, (200, 200, 0)), (10, 10))
    update_inventory()
    
    pygame.display.update()
    fpsClock.tick(fps)

pygame.quit()
sys.exit()
