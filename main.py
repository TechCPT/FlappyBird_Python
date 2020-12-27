# import modules
import pygame
import sys


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 450))
    screen.blit(floor_surface, (floor_x_pos + 288, 450))


pygame.init()  # initializes all imported pygame modules
# creates display surface stored in the screen variable, passes tuple of width and height as argument
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()  # allows the limitation of frame rate

# Game Variables
gravity = 0.25
bird_movement = 0

# import surface image and store in bg_surface variable
# convert isn't strictly necessary but it converts the image into a type of file that is easier to work with for pygame
bg_surface = pygame.image.load("assets/background-day.png").convert()

floor_surface = pygame.image.load("assets/base.png").convert()
floor_x_pos = 0

bird_surface = pygame.image.load("assets/bluebird-midflap.png").convert()
bird_rect = bird_surface.get_rect(center=(50, 256))

''' --- GAME LOOP --- '''
while True:
    ''' --- EVENT LOOP --- '''
    # Pygame looks for all the events currently happening, ex. moving the mouse, pressing a button, closing a window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # looks for closing of the game with the X button
            pygame.quit()  # uninitializes all pygame modules
            sys.exit()  # shuts down the game completely, ends code
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 6


    # Puts one surface on another surface, sets location of top-left corner of surface (x, y) coordinates
    screen.blit(bg_surface, (0, 0))

    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)

    floor_x_pos -= 1  # increments x position of floor surface
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0

    pygame.display.update()  # Takes anything drawn within the while loop and draws it on the screen
    clock.tick(120)  # limit frame rate, cannot run faster than 120 fps
