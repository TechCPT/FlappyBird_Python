# import modules
import pygame
import sys

pygame.init()  # initializes all imported pygame modules
# creates display surface stored in the screen variable, passes tuple of width and height as argument
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()  # allows the limitation of frame rate

# import surface image and store in bg_surface variable
# convert isn't strictly necessary but it converts the image into a type of file that is easier to work with for pygame
bg_surface = pygame.image.load("assets/background-day.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)  # doubles size of background surface

''' --- GAME LOOP --- '''
while True:
    ''' --- EVENT LOOP --- '''
    # Pygame looks for all the events currently happening, ex. moving the mouse, pressing a button, closing a window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # looks for closing of the game with the X button
            pygame.quit()  # uninitializes all pygame modules
            sys.exit()  # shuts down the game completely, ends code

    # Puts one surface on another surface, sets location of top-left corner of surface (x, y) coordinates
    screen.blit(bg_surface, (0, 0))

    pygame.display.update()  # Takes anything drawn within the while loop and draws it on the screen
    clock.tick(120)  # limit frame rate, cannot run faster than 120 fps
