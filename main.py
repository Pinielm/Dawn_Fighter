
import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dawn_1')

# set frame rate
clock = pygame.time.Clock()
FPS = 60

# definen colors
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

# define game variables 
intro_count = 3
last_count_update = pygame.time.get_ticks()

# define fighter variables 
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72,56]
WARRIOR_DATA = [WARRIOR_SIZE,WARRIOR_SCALE,WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112,107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE,WIZARD_OFFSET]

#bg image
bg_image = pygame.image.load(r"assets/images/background/background.jpg").convert_alpha()

#load sprite sheets
warrior_sheet = pygame.image.load(r"assets/images/Warrior/Warrior/Sprites/Warrior.png").convert_alpha()
wizard_sheet = pygame.image.load(r"assets/images/Wizard/Wizard/Sprites/Wizard.png").convert_alpha()

#define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10,8,3,7,7,3,3,7,8]
WIZARD_ANIMATION_STEPS = [8,8,2,8,8,3,2,7]
#function to draw the background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

def draw_health_bar(health, x,y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x-2,y-2, 404 , 34))
    pygame.draw.rect(screen, RED, (x,y, 400 , 30))
    pygame.draw.rect(screen, YELLOW, (x,y, 400 * ratio , 30))

# create instances of fighters
fighter_1 = Fighter(1,200, 310, False, WARRIOR_DATA,warrior_sheet, WARRIOR_ANIMATION_STEPS)
fighter_2 = Fighter(2,700, 310,True, WIZARD_DATA,wizard_sheet, WIZARD_ANIMATION_STEPS)

#game loop
run = True

while run:

    clock.tick(FPS)

    # draw the background
    draw_bg()

    # show player stats
    draw_health_bar(fighter_1.health, 20,20)
    draw_health_bar(fighter_2.health, 580,20)

    # update  countdown
    if intro_count <= 0:
        #move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)
    else:
        #update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()
            print(intro_count)


    # update fighters
    fighter_1.update()
    fighter_2.update()

    # draw fighters 
    fighter_1.draw(screen)
    fighter_2.draw(screen)


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

#exit game
pygame.quit