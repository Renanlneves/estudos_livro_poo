# pygame demo 2 - one image, click and move

import pygame
from pygame.locals import *
import sys
import random


#2 - definindo constantes 
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100  
N_PIXELS_PER_FRAME = 3

#3 - inicia o mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 carregar recursos: imagens, sons, etc
ballImage = pygame.image.load('images/ball.png')

#5 iniciando variaveis 
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)

xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME



#6 - loop infinito
while True:

    #7 - check for and handle events
    for event in pygame.event.get():
        #clicked the close button? quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

        

    # 8 do any "per frame" actions

    if (ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed #reverse the x direction
    
    if (ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed #reverse the y direction

    #update the ball's location, using the speed in two directions 
    ballX = ballX + xSpeed
    ballY = ballY + ySpeed


    #9 clear the window
    window.fill(BLACK)

    #10 - Draw all window elements
    # draw ball at position 100 across (x) and 200 down (y)
    window.blit(ballImage, (ballX, ballY))

    #11 - update the window
    pygame.display.update()

    #12 - slow things down a bit
    clock.tick(FRAMES_PER_SECOND) #make pygame wait

    