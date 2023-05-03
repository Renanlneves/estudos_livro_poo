# pygame demo 1 – draw one image

import pygame
from pygame.locals import *
import sys

#2 - definindo constantes 
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

#3 - inicia o mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 carregar recursos: imagens, sons, etc
ballImage = pygame.image.load('images/ball.png')

#5 iniciando variaveis 

#6 - loop infinito
while True:

    #7 - check for and handle events
    for event in pygame.event.get():
        #clicked the close button? quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 do any "per frame" actions

    #9 clear the window
    window.fill(BLACK)

    #10 - Draw all window elements
    # draw ball at position 100 across (x) and 200 down (y)
    window.blit(ballImage, (100, 200))

    #11 - update the window
    pygame.display.update()

    #12 - slow things down a bit
    clock.tick(FRAMES_PER_SECOND) #make pygame wait

    