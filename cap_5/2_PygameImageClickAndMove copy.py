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

BALL_WIDTH_HEIGHT = 100  # COMENTARIO 2 DO LIVRO
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

#3 - inicia o mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 carregar recursos: imagens, sons, etc
ballImage = pygame.image.load('images/ball.png')

#5 iniciando variaveis 
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)

ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

#6 - loop infinito
while True:

    #7 - check for and handle events
    for event in pygame.event.get():
        #clicked the close button? quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #see if the user clicked
        if event.type == pygame.MOUSEBUTTONUP:
            # mouseX, mouseY = event.pos #could do this if we needed it
            #check if the click was in the rect of the ball
            #if so, choose a randon new location

            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)


    # 8 do any "per frame" actions

    #9 clear the window
    window.fill(BLACK)

    #10 - Draw all window elements
    # draw ball at position 100 across (x) and 200 down (y)
    window.blit(ballImage, (ballX, ballY))

    #11 - update the window
    pygame.display.update()

    #12 - slow things down a bit
    clock.tick(FRAMES_PER_SECOND) #make pygame wait

    