import pygame
import sys
import random


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 675))
    screen.blit(floor_surface, (floor_x_pos + 432, 675))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(525, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(525, random_pipe_pos - 225))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 768:  # checks if the pipe is the bottom one
            screen.blit(pipe_surface, pipe)
        else:
            # pygame.transform.flip(surface, x position, y position)
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):  # check if bird rectangle is colliding with any of the pipe rectangles
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 675:
        return False

    return True


def rotatebird(bird):
    # pygame.transform.rotozoom(surface, angle, scale)
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird


def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect


pygame.init()  # initializes all imported pygame modules
# creates display surface stored in the screen variable, passes tuple of width and height as argument
screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()  # allows the limitation of frame rate

# Game Variables
gravity = 0.25
bird_movement = 0
game_active = True

# convert isn't strictly necessary but it converts the image into a type of file that is easier to work with for pygame
bg_surface = pygame.image.load("assets/background-day.png").convert()
bg_surface = pygame.transform.scale(bg_surface, (432, 768))

floor_surface = pygame.image.load("assets/base.png").convert()
floor_surface = pygame.transform.scale(floor_surface, (504, 168))
floor_x_pos = 0

bird_downflap = pygame.transform.scale((pygame.image.load("assets/bluebird-downflap.png").convert_alpha()), (51, 36))
bird_midflap = pygame.transform.scale((pygame.image.load("assets/bluebird-midflap.png").convert_alpha()), (51, 36))
bird_upflap = pygame.transform.scale((pygame.image.load("assets/bluebird-upflap.png").convert_alpha()), (51, 36))
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 384))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

# bird_surface = pygame.image.load("assets/bluebird-midflap.png").convert_alpha()
# bird_surface = pygame.transform.scale(bird_surface, (51, 36))
# bird_rect = bird_surface.get_rect(center=(100, 384))

pipe_surface = pygame.image.load("assets/pipe-green.png").convert()
pipe_surface = pygame.transform.scale(pipe_surface, (78, 480))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [300, 450, 600]


''' --- GAME LOOP --- '''
while True:
    ''' --- EVENT LOOP --- '''
    # Pygame looks for all the events currently happening, ex. moving the mouse, pressing a button, closing a window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # looks for closing of the game with the X button
            pygame.quit()  # uninitializes all pygame modules
            sys.exit()  # shuts down the game completely, ends code
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 9
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()  # despawn all pipes
                bird_rect.center = (100, 384)  # reset bird position
                bird_movement = 0  # reset bird movement

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()

    # Puts one surface on another surface, sets location of top-left corner of surface (x, y) coordinates
    screen.blit(bg_surface, (0, 0))

    if game_active:
        # Bird
        bird_movement += gravity
        rotated_bird = rotatebird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

    # Floor
    floor_x_pos -= 1  # increments x position of floor surface
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0

    pygame.display.update()  # Takes anything drawn within the while loop and draws it on the screen
    clock.tick(120)  # limit frame rate, cannot run faster than 120 fps
